#!/usr/bin/env python3
"""Build source-verified vocabulary evidence; never modify corpus sources."""
import argparse, collections, hashlib, importlib.util, json, re
from pathlib import Path

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--manifest',type=Path,required=True)
    ap.add_argument('--choices',type=Path,required=True)
    ap.add_argument('--root',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args()
    spec=importlib.util.spec_from_file_location('style_corpus',Path(__file__).with_name('style_corpus.py'))
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    manifest=json.loads(a.manifest.read_text())
    choices=json.loads(a.choices.read_text())
    root=a.root; inventory={}; texts=[]
    for protected in (root,):
        if a.output.resolve().is_relative_to(protected.resolve()):
            ap.error('Output must be outside source roots')
    for rec in manifest['records']:
        if rec['role'] not in ('primary','historical'): continue
        raw=mod.read_record(root,rec); plain=mod.prose(raw)
        texts.append((rec,raw,plain))
        counts=collections.Counter(re.findall(r'\b[a-z]+\b',plain))
        for word,count in counts.items():
            item=inventory.setdefault(word,{'primary_occurrences':0,'primary_works':[], 'historical_occurrences':0,'historical_sources':[], 'examples':[]})
            key='primary' if rec['role']=='primary' else 'historical'
            item[key+'_occurrences']+=count
            item['primary_works' if key=='primary' else 'historical_sources'].append(rec['id'])
    def examples(phrase, selected, limit):
        out=[]; pat=re.compile(r'\b'+r'\s+'.join(map(re.escape,phrase.split()))+r'\b',re.I)
        for rec,raw,plain in selected:
            if not pat.search(plain): continue
            # Keep exact source paragraph and line offsets. No generated sentences.
            for block in re.finditer(r'[^\n](?:.*?)(?=\n\s*\n|\Z)',raw,re.S):
                if not pat.search(mod.prose(block.group())): continue
                match=pat.search(mod.visible_source(block.group()))
                if not match: continue
                lines=raw.splitlines(keepends=True)
                hit=raw.count('\n',0,block.start()+match.start())
                last=raw.count('\n',0,block.start()+match.end())
                lo=max(0,hit-2); hi=min(len(lines),last+5)
                excerpt=''.join(lines[lo:hi]).removesuffix('\n')
                out.append({'source':rec['id'],'role':rec['role'],'path':rec['path'], 'sha256':rec['sha256'], 'line_start':lo+1,'line_end':hi,'raw_tex':excerpt})
                break
            if len(out)>=limit: break
        return out
    primary=[t for t in texts if t[0]['role']=='primary']
    for word,item in inventory.items():
        item['examples']=examples(word,primary,2) or examples(word,texts,1)
    entries=[]
    for i,(trigger,target,role,condition) in enumerate(choices,1):
        pat=re.compile(r'\b'+re.escape(target)+r'\b',re.I)
        support=[r['id'] for r,raw,plain in primary if pat.search(plain)]
        ev=examples(target,primary,2)
        if not support or not ev: raise ValueError('No primary evidence: '+target)
        entries.append(dict(id=f'L{i:02}',search_terms=trigger,target=target,role=role,condition=condition,primary_works=support,examples=ev))
    a.output.mkdir(parents=True,exist_ok=True)
    meta={'schema':1,'extraction':'Heuristic English surface forms, lowercase; TeX macros not expanded; no lemmatization; formula/preamble/bibliography masking from style_corpus.py. Not an approved vocabulary whitelist.', 'primary_works':len(primary),'historical_sources':len(texts)-len(primary), 'primary_tokens':sum(x['primary_occurrences'] for x in inventory.values()), 'primary_surface_forms':sum(bool(x['primary_occurrences']) for x in inventory.values()), 'manifest_sha256':hashlib.sha256(a.manifest.read_bytes()).hexdigest()}
    (a.output/'vocabulary-index.json').write_text(json.dumps({'metadata':meta,'words':dict(sorted(inventory.items()))},ensure_ascii=False,indent=2)+'\n')
    (a.output/'contextual-lexicon.json').write_text(json.dumps({'metadata':meta,'candidate_status':'Editor-proposed alternatives, not observed revision pairs; search terms are not asserted absent or forbidden. Targets are corpus-attested.', 'entries':entries},ensure_ascii=False,indent=2)+'\n')
    md=['# Contextual vocabulary evidence', '',
        'Private source excerpts. Review before sharing. Counts are heuristic, not a vocabulary whitelist.', '',
        'Proposed alternatives are editorial suggestions, not observed revision pairs.', '',
        f"Primary works: {len(primary)}. Historical sources: {len(texts)-len(primary)}.", '',
        '| ID | Search terms | Candidate | Role | Primary support |',
        '| --- | --- | --- | --- | --- |']
    for e in entries: md.append(f"| {e['id']} | {e['search_terms']} | {e['target']} | {e['role']} | {len(e['primary_works'])}/{len(primary)} |")
    for e in entries:
        md += ['',f"## {e['id']} — {e['target']}",'',f"検索語: {e['search_terms']}",'',f"使う文脈: {e['role']}。{e['condition']}",'']
        ev=min(e['examples'],key=lambda x:len(x['raw_tex'])); md += [f"実例: `{ev['source']}`、元 TeX {ev['line_start']}–{ev['line_end']} 行。相対パス: `{ev['path']}`。",'', '```tex', ev['raw_tex'], '```']
    (a.output/'contextual-lexicon.md').write_text('\n'.join(md)+'\n')
    print(json.dumps(meta,ensure_ascii=False)); print('entries',len(entries))
if __name__=='__main__': main()
