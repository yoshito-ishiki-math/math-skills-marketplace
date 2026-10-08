#!/usr/bin/env python3
"""Copy the bundled package into an existing manuscript directory, without overwriting."""
import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', type=Path)
    args = parser.parse_args()
    if not args.directory.is_dir():
        parser.error('target must be an existing manuscript directory')
    source = Path(__file__).resolve().parents[1] / 'assets' / 'paragraphids.sty'
    target = args.directory / source.name
    data = source.read_bytes()
    if target.is_symlink():
        parser.error('refusing a symlink target')
    if target.exists():
        if target.is_file() and target.read_bytes() == data:
            print(f'Already current: {target}')
            return
        parser.error('existing package differs; inspect and preserve local changes before updating')
    with target.open('xb') as output:
        output.write(data)
    print(f'Installed: {target}')

if __name__ == '__main__':
    main()
