"""Synthetic checks: no real manuscripts or author corpus is required."""
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / 'skills/write-research-paper/scripts'
spec = importlib.util.spec_from_file_location('style_corpus', SCRIPTS/'style_corpus.py')
corpus = importlib.util.module_from_spec(spec)
spec.loader.exec_module(corpus)


class PortableToolsTests(unittest.TestCase):
    def run_script(self, path, *args, ok=True):
        result = subprocess.run([sys.executable, str(path), *map(str,args)], capture_output=True, text=True)
        if ok:
            self.assertEqual(result.returncode, 0, result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0)
        return result

    def test_corpus_build_and_lookup_without_personal_data(self):
        with tempfile.TemporaryDirectory() as temp:
            base=Path(temp); source=base/'sources';source.mkdir()
            raw=b'\\documentclass{article}\n\\begin{document}\nWe obtain the desired bound.\n\nIt remains to prove the assertion.\n\\end{document}\n'
            (source/'sample.tex').write_bytes(raw)
            record=dict(id='sample',work='sample',role='primary',path='sample.tex',sha256=hashlib.sha256(raw).hexdigest())
            manifest=base/'manifest.json';manifest.write_text(json.dumps({'records':[record]}))
            choices=base/'choices.json';choices.write_text(json.dumps([['derive','obtain','inference','Only when the meaning matches.']]))
            args=['--manifest',manifest,'--root',source]
            self.run_script(SCRIPTS/'style_corpus.py',*args)
            build=[*args,'--choices',choices,'--output',base/'output']
            self.run_script(SCRIPTS/'build_lexicon.py',*build)
            report=json.loads(self.run_script(SCRIPTS/'lookup_lexicon.py','--references',base/'output','--word','obtain').stdout)
            self.assertEqual(report['evidence']['primary_occurrences'],1)
            self.assertEqual(report['evidence']['examples'][0]['path'],'sample.tex')
            self.assertEqual((source/'sample.tex').read_bytes(),raw)
            self.run_script(SCRIPTS/'build_lexicon.py',*args,'--choices',choices,'--output',source/'output',ok=False)
            (source/'sample.tex').write_bytes(raw+b'% changed\n')
            self.run_script(SCRIPTS/'style_corpus.py',*args,ok=False)

    def test_corpus_path_escape_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)/'source';root.mkdir()
            with self.assertRaisesRegex(ValueError,'escapes'):
                corpus.read_record(root,{'path':'../outside.tex','sha256':'0'*64,'id':'test'})

    # Paragraph-ID runtime coverage lives in Kicho alongside its implementation.
    def test_local_markdown_links_resolve(self):
        import re
        for path in (ROOT/'skills').rglob('*.md'):
            for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',path.read_text()):
                if '://' in target or target.startswith('#'):
                    continue
                self.assertTrue((path.parent/target.split('#')[0]).exists(),f'{path}: {target}')


if __name__=='__main__':unittest.main()
