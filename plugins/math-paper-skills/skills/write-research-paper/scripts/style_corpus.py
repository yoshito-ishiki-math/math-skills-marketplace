#!/usr/bin/env python3
"""Read-only, standard-library retrieval and lexical diagnostics for author style.

No TeX execution, source writes, network calls, or automatic manuscript edits.
Reports are heuristic, not a grammar parser or a measure of authorship.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re


PHRASES = (
    'we denote by', 'we denote', 'we write', 'we define', 'we say that',
    'is said to be', 'we prove that', 'we show that', 'we obtain',
    'we first', 'we next', 'we shall', 'in this paper', 'in the present paper',
    'in this section', 'in what follows', 'it suffices to', 'it remains to',
    'we need only', 'we may assume that', 'assume that', 'suppose that',
    'for the sake of contradiction', 'by applying', 'according to',
    'it follows that', 'this implies that', 'note that', 'notice that',
    'therefore', 'thus', 'hence', 'then', 'since', 'provided that',
    'in particular', 'as a consequence', 'as an application', 'in other words',
    'conversely', 'we conclude that', 'we complete the proof',
)
ROLES = {
    'notation': r'\b(?:we denote|we write|we define|put|set)\b',
    'definition': r'\b(?:we say that|is said to be|is called)\b',
    'contribution': r'\b(?:in this paper|in the present paper|we prove that|we show that)\b',
    'proof-goal': r'\b(?:it suffices to|it remains to|we need only|we shall prove|we next prove)\b',
    'contradiction': r'\b(?:for the sake of contradiction|contradiction)\b',
    'cases': r'\b(?:case|conversely|on the other hand)\b',
    'inference': r'\b(?:by applying|according to|since|therefore|thus|hence)\b',
    'closure': r'\b(?:we conclude|this completes|we complete|this finishes|this proves)\b',
}


def visible_source(text):
    """Keep source offsets while masking comments, preamble, and bibliography."""
    # A % preceded by an odd number of backslashes is escaped.
    chars = list(text)
    for m in re.finditer('%', text):
        k = m.start() - 1
        while k >= 0 and text[k] == '\\':
            k -= 1
        if (m.start() - 1 - k) % 2:
            continue
        end = text.find('\n', m.start())
        end = len(text) if end < 0 else end
        chars[m.start():end] = ' ' * (end - m.start())
    text = ''.join(chars)
    begin = re.search(r'\\begin\{document\}', text)
    if begin:
        text = re.sub(r'[^\n]', ' ', text[:begin.end()]) + text[begin.end():]
    end = re.search(r'\\(?:begin\{thebibliography\}|bibliography\{|printbibliography|end\{document\})', text)
    if end:
        text = text[:end.start()] + re.sub(r'[^\n]', ' ', text[end.start():])
    for m in list(re.finditer(r'\\begin\{(?:comment|verbatim|lstlisting)\}.*?\\end\{(?:comment|verbatim|lstlisting)\}', text, re.S)):
        text = text[:m.start()] + re.sub(r'[^\n]', ' ', m.group()) + text[m.end():]
    return text


def prose(text):
    text = visible_source(text)
    # Boundaries, rather than deletion, prevent collocations across mathematics.
    text = re.sub(r'\$\$.*?\$\$|(?<!\\)\$.*?(?<!\\)\$|\\\[.*?\\\]|\\\(.*?\\\)', ' | ', text, flags=re.S)
    text = re.sub(r'\\begin\{(equation\*?|align\*?|gather\*?|eqnarray\*?|displaymath)\}.*?\\end\{\1\}', ' | ', text, flags=re.S)
    text = re.sub(r'\\[A-Za-z@]+\*?(?:\[[^\]]*\])?(?:\{[^{}]*\})?', ' | ', text)
    return re.sub(r'\s+', ' ', text).lower()


def read_record(root, record):
    path = (root / record['path']).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError('Source path escapes corpus root')
    data = path.read_bytes()
    if hashlib.sha256(data).hexdigest() != record['sha256']:
        raise ValueError('Source changed; review and refresh manifest: ' + record['id'])
    try:
        return data.decode('utf-8-sig')
    except UnicodeDecodeError:
        raise ValueError('Non-UTF-8 source needs explicit encoding review: ' + record['id'])


def summarize(records, root):
    reports = []
    for record in records:
        text = read_record(root, record)
        plain = prose(text)
        counts = {p: len(re.findall(r'\b' + re.escape(p) + r'\b', plain)) for p in PHRASES}
        grams = Counter()
        # Preserve punctuation and formula boundaries. No synthetic joining.
        for segment in re.split(r'[^a-z\s\x27-]', plain):
            words = re.findall(r"[a-z]+(?:'[a-z]+)?", segment)
            for n in range(2, 6):
                grams.update(' '.join(words[i:i+n]) for i in range(len(words)-n+1))
        reports.append({'id': record['id'], 'work': record['work'], 'role': record['role'],
                        'english_tokens': len(re.findall(r'\b[a-z]+\b', plain)),
                        'phrases': counts, 'top_ngrams': grams.most_common(35),
                        'unexpanded_inputs': re.findall(r'\\(?:input|include)\s*\{([^}]+)\}', visible_source(text))})
    primary = [r for r in reports if r['role'] == 'primary']
    if len({r['work'] for r in primary}) != len(primary):
        raise ValueError('More than one primary source for a work')
    support = {p: [r['id'] for r in primary if r['phrases'][p]] for p in PHRASES}
    return {'primary_works': len(primary), 'support_by_work': support, 'records': reports}


def retrieve(records, root, role, limit, selected):
    result = []
    pattern = re.compile(ROLES[role], re.I)
    for record in records:
        if selected and record['id'] != selected:
            continue
        if not selected and record['role'] != 'primary':
            continue
        text = read_record(root, record)
        visible = visible_source(text)
        per_work = 0
        for match in pattern.finditer(visible):
            start = text.rfind('\n\n', 0, match.start()) + 2
            if start == 1:
                start = 0
            end = text.find('\n\n', match.end())
            end = len(text) if end < 0 else end
            # Bound long source paragraphs; raw TeX is explicitly a fragment.
            start = max(start, text.rfind('\n', 0, max(start, match.start()-250))+1)
            end = min(end, match.end()+650)
            result.append({'id': record['id'], 'role': role, 'path': record['path'],
                           'line_start': text.count('\n', 0, start)+1,
                           'line_end': text.count('\n', 0, end)+1,
                           'raw_tex_fragment': text[start:end]})
            per_work += 1
            if per_work >= limit:
                break
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', type=Path, required=True)
    parser.add_argument('--root', type=Path, required=True, help='Private corpus root')
    parser.add_argument('--role', choices=ROLES)
    parser.add_argument('--work', help='Exact source ID, including -old for a historical source')
    parser.add_argument('--limit', type=int, default=2, help='Matches per work for retrieval')
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text())
    root = args.root
    records = manifest['records']
    if args.limit < 1:
        parser.error('--limit must be positive')
    if args.work and args.work not in {r['id'] for r in records}:
        parser.error('Unknown source ID')
    result = retrieve(records, root, args.role, args.limit, args.work) if args.role else summarize(records, root)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
