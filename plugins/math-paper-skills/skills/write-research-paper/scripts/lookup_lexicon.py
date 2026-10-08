#!/usr/bin/env python3
"""Look up contextual alternatives or exact surface-form evidence (read-only)."""
import argparse,json
from pathlib import Path

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('query',nargs='?',default='')
    p.add_argument('--word',help='Exact English surface form, case insensitive')
    p.add_argument('--references',type=Path,required=True)
    a=p.parse_args()
    if a.word:
        data=json.loads((a.references/'vocabulary-index.json').read_text())
        word=a.word.lower().strip()
        print(json.dumps({'word':word,'evidence':data['words'].get(word),'absence_note':'A missing surface form is not a ban or evidence about the whole archive.'},ensure_ascii=False,indent=2))
    else:
        data=json.loads((a.references/'contextual-lexicon.json').read_text())
        q=a.query.casefold()
        entries=[e for e in data['entries'] if q in ' '.join(str(e[k]) for k in ('id','search_terms','target','role','condition')).casefold()]
        print(json.dumps({'candidate_status':data['candidate_status'],'entries':entries},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
