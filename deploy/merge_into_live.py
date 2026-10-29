#!/usr/bin/env python3
"""DEPRECATED / LEGACY (marked 2026-10-29): three-way merge into the LIVE data.json
of the retired van7_sklad warehouse (Flask :5055, deleted 2026-10-16).

The live target no longer exists, so this script has nothing to merge into.
Kept for history only — do not run. The catalog now lives in this repository:
data.json is the single source of truth.

Original purpose:
BASE = catalog at the commit the changes were made on,
NEW = catalog on GitHub main, LIVE = file on the server.

 - item in NEW but not in LIVE and not in BASE  -> added (new tool)
 - item in both, LIVE.desc == BASE.desc          -> desc taken from NEW (translation)
 - item in both, LIVE.desc != BASE.desc          -> kept as on the server (edited there), reported
 - same rules for item name and category name
 - items only on the server stay untouched (reported, so they can be translated later)
 - nothing is ever deleted; a timestamped backup is written before any change
Usage: merge_into_live.py LIVE NEW BASE [--write]   (LIVE/NEW/BASE: path or URL; dry-run by default)
"""
import json, shutil, sys, os, time, tempfile, urllib.request

def load(src):
    if src.startswith(('http://', 'https://')):
        with urllib.request.urlopen(src, timeout=60) as r:
            return json.loads(r.read().decode('utf-8'))
    with open(src, encoding='utf-8') as f:
        return json.load(f)

def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    write = '--write' in sys.argv
    live_path, new_src, base_src = args
    live, new, base = load(live_path), load(new_src), load(base_src)
    L = {str(i['id']): i for i in live['items']}
    B = {str(i['id']): i for i in base['items']}
    LC = {c['id']: c for c in live['cats']}
    BC = {c['id']: c for c in base['cats']}
    rep = {'added': [], 'skipped_added': [], 'desc_updated': 0, 'desc_kept': [],
           'name_updated': 0, 'name_kept': [], 'cat_updated': 0, 'cat_kept': [], 'server_only': []}
    for it in new['items']:
        k = str(it['id'])
        if k not in L:
            if k in B:
                continue  # existed in base, deleted on the server on purpose: do not resurrect
            if it.get('cat') in LC:
                live['items'].append(it); L[k] = it; rep['added'].append(it['name'])
            else:
                rep['skipped_added'].append((it['name'], it.get('cat')))
            continue
        cur, b = L[k], B.get(k)
        if b is None:
            continue
        for f, upd, kept in (('desc', 'desc_updated', 'desc_kept'), ('name', 'name_updated', 'name_kept')):
            if it.get(f) == cur.get(f):
                continue
            if cur.get(f) == b.get(f):
                cur[f] = it[f]; rep[upd] += 1
            else:
                rep[kept].append(k)
    for c in new['cats']:
        cur, b = LC.get(c['id']), BC.get(c['id'])
        if cur is None or b is None or c['name'] == cur['name']:
            continue
        if cur['name'] == b['name']:
            cur['name'] = c['name']; rep['cat_updated'] += 1
        else:
            rep['cat_kept'].append(c['id'])
    nk = {str(i['id']) for i in new['items']}
    rep['server_only'] = [(k, L[k].get('name')) for k in L if k not in nk]
    print('added %d, desc updated %d, name updated %d, cat names updated %d' % (
        len(rep['added']), rep['desc_updated'], rep['name_updated'], rep['cat_updated']))
    for key in ('skipped_added', 'desc_kept', 'name_kept', 'cat_kept', 'server_only'):
        print('%s (%d): %s' % (key, len(rep[key]), rep[key][:20]))
    print('total items now:', len(live['items']), 'cats:', len(live['cats']))
    if not write:
        print('DRY RUN: nothing written'); return
    d = os.path.dirname(os.path.abspath(live_path))
    os.makedirs(os.path.join(d, 'backups'), exist_ok=True)
    bk = os.path.join(d, 'backups', 'data_%s_pre_en_merge.json' % time.strftime('%Y%m%d_%H%M%S'))
    shutil.copy2(live_path, bk); print('backup:', bk)
    text = json.dumps(live, ensure_ascii=False, indent=2)
    json.loads(text)
    fd, tmp = tempfile.mkstemp(dir=d, suffix='.tmp')
    with os.fdopen(fd, 'w', encoding='utf-8') as f:
        f.write(text)
    os.chmod(tmp, os.stat(live_path).st_mode & 0o777)
    os.replace(tmp, live_path)
    print('written:', live_path)

main()
