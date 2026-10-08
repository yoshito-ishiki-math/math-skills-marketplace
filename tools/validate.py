#!/usr/bin/env python3
"""Validate distributable package paths and the recorded public source snapshot."""
import hashlib
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def packaged_path(base, relative):
    require(isinstance(relative, str) and relative.startswith("./"),
            f"Expected a ./-prefixed path: {relative!r}")
    target = (base / relative).resolve()
    require(target.is_relative_to(base.resolve()), f"Path escapes package: {relative}")
    require(target.exists(), f"Missing packaged path: {relative}")
    return target


def main():
    catalog = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text())
    provenance = json.loads((ROOT / "UPSTREAM.json").read_text())
    require(catalog["name"] == "yoshito-ishiki-math", "Unexpected marketplace name")
    require(len(catalog["plugins"]) == 1, "Expected the initial single-plugin catalog")
    entry = catalog["plugins"][0]
    require(entry["source"]["source"] == "local", "Expected a bundled plugin source")
    require(entry["policy"] == {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
            "Unexpected install policy")
    plugin = packaged_path(ROOT, entry["source"]["path"])
    manifest = json.loads((plugin / "plugin.json").read_text())
    require(manifest["$schema"] == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
            "Unexpected portable manifest schema")
    require(entry["name"] == manifest["name"] == provenance["plugin"], "Plugin names differ")
    require(manifest["version"] == provenance["plugin_version"], "Plugin versions differ")
    require(re.fullmatch(r"\d+\.\d+\.\d+", manifest["version"]), "Invalid version")
    interface = manifest["extensions"]["com.openai"]["interface"]
    require(interface["category"] == entry["category"], "Plugin categories differ")
    for field, limit in [("displayName", 30), ("shortDescription", 30),
                         ("longDescription", 4000), ("developerName", 80)]:
        text = interface[field]
        require(isinstance(text, str) and 0 < len(text) <= limit, f"Invalid {field}")
    require(0 < len(interface["defaultPrompt"]) <= 3, "Invalid prompt count")
    require(all(0 < len(prompt) <= 128 for prompt in interface["defaultPrompt"]),
            "Invalid default prompt length")
    for field in ["logo", "composerIcon"]:
        icon = packaged_path(plugin, interface[field])
        svg = ET.parse(icon).getroot()
        view_box = [float(v) for v in svg.attrib["viewBox"].split()]
        require(view_box[2] == view_box[3] and view_box[2] >= 48, "Invalid icon dimensions")
    for field in ["homepage", "repository"]:
        require(manifest[field].startswith("https://"), f"Invalid {field}")
    require(manifest["license"] == "MIT" and (plugin / "LICENSE").is_file(), "Missing license")
    require(re.fullmatch(r"[a-f0-9]{40}", provenance["revision"]), "Invalid source revision")

    imported = set()
    for item in provenance["files"]:
        relative = Path(item["path"])
        require(not relative.is_absolute() and ".." not in relative.parts, "Invalid source path")
        require(item["path"] not in imported, f"Duplicate source path: {relative}")
        imported.add(item["path"])
        path = plugin / relative
        require(path.is_file() and not path.is_symlink(), f"Missing or linked source: {relative}")
        raw = path.read_bytes()
        require(len(raw) == item["size"], f"Source size changed: {relative}")
        require(hashlib.sha256(raw).hexdigest() == item["sha256"], f"Source hash changed: {relative}")
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        require(blob == item["git_blob_sha1"], f"Source blob changed: {relative}")

    expected = {"write-research-paper", "read-research-paper", "latex-paragraph-ids"}
    skills = list((plugin / "skills").glob("*/SKILL.md"))
    require({skill.parent.name for skill in skills} == expected, "Unexpected skill set")
    for skill in skills:
        source = skill.read_text()
        require(source.startswith("---\n"), f"Missing frontmatter: {skill}")
        frontmatter = source.split("---", 2)[1]
        require(re.search(rf"^name: {re.escape(skill.parent.name)}$", frontmatter, re.M),
                f"Skill name differs from directory: {skill}")
        require(re.search(r"^description: .+", frontmatter, re.M), f"Missing description: {skill}")

    links = 0
    for markdown in (plugin / "skills").rglob("*.md"):
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", markdown.read_text()):
            if ":" in target or target.startswith(("#", "/")):
                continue
            relative = target.split("#", 1)[0]
            if not relative:
                continue
            path = (markdown.parent / relative).resolve()
            require(path.is_relative_to(plugin.resolve()), f"Skill link escapes plugin: {target}")
            require(path.exists(), f"Broken skill link in {markdown.relative_to(ROOT)}: {target}")
            links += 1

    for path in ROOT.rglob("*"):
        if ".git" in path.parts or "__pycache__" in path.parts:
            continue
        require(not path.is_symlink(), f"Distribution contains a symlink: {path}")
        if path.is_file():
            require(not re.search(rb"/(?:Users|home)/[A-Za-z0-9._-]+/", path.read_bytes()),
                    f"Distribution contains a local home path: {path}")
    print(f"Validated {len(skills)} skills, {len(imported)} unchanged source files, "
          f"{links} skill links, catalog metadata, and icons.")


if __name__ == "__main__":
    main()
