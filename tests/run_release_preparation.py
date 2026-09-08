#!/usr/bin/env python3
"""Isolated technical preparation regression; run directly like run_e2e.py."""
import hashlib, json, pathlib, runpy, shutil, subprocess, sys, tempfile
import yaml
repo = pathlib.Path(__file__).resolve().parents[1]
warning = ('WARNING: This script performs technical preparation only. It does NOT '
           'verify Founder ratification in the UFD ledger. Institutional release '
           'requires explicit ledger approval.')
def hashes(root):
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob('*') if p.is_file()}
def run(script, cwd, *args):
    result = subprocess.run([sys.executable, str(script), *args], cwd=cwd, capture_output=True, text=True)
    print(f'COMMAND: {script.name} {" ".join(args)}\nEXIT: {result.returncode}\nSTDOUT: {result.stdout}STDERR: {result.stderr}')
    return result
with tempfile.TemporaryDirectory(prefix='w2b-verify-') as tmp:
    root = pathlib.Path(tmp)
    modified = root / 'modified'
    modified.mkdir()
    shutil.copytree(repo / 'ckm-staging', modified / 'ckm-staging')
    shutil.copytree(repo / 'governance', modified / 'governance')
    before = hashes(modified)
    script = repo / 'cut_release.py'
    result = run(script, modified)
    assert result.returncode == 2 and warning in result.stderr
    assert hashes(modified) == before and not (modified / 'ckm-2.0.0-alpha').exists()
    print('PASS: missing acknowledgment fails closed before any writes')
    result = run(script, modified, '--acknowledge-technical-only', '--unknown')
    assert result.returncode == 2 and hashes(modified) == before
    print('PASS: invalid arguments fail before writes')
    result = run(script, modified, '--help')
    assert result.returncode == 0 and ' '.join(warning.split()) in ' '.join(result.stdout.split())
    assert hashes(modified) == before
    result = run(script, modified, '--acknowledge-technical-only')
    assert result.returncode == 0 and warning in result.stderr
    assert 'TECHNICAL SNAPSHOT PREPARED' in result.stdout
    assert hashes(modified / 'ckm-staging') == hashes(repo / 'ckm-staging')
    assert hashes(modified / 'governance') == hashes(repo / 'governance')
    dst = modified / 'ckm-2.0.0-alpha'
    manifest = json.loads((dst / 'release_manifest.json').read_text())
    assert 'ratified_by' not in manifest
    assert manifest['preparation_scope'] == 'technical-only; Founder ratification not verified'
    assert manifest['dataset_scope'] == 'ckm-staging overlay only; not a complete merged CKM release'
    assert set(manifest) == {'ckm_release', 'cut', 'canonical_name', 'namespace',
                             'preparation_scope', 'dataset_scope', 'objects', 'files'}
    assert 'not a complete merged CKM release' in result.stdout
    count = 0
    for src in (modified / 'ckm-staging').rglob('*'):
        if not src.is_file(): continue
        rel = src.relative_to(modified / 'ckm-staging')
        obj = yaml.safe_load(src.read_text())
        if isinstance(obj, dict) and 'id' in obj:
            count += 1
            expected = dict(obj, ckm_release='2.0.0-alpha')
            assert yaml.safe_load((dst / rel).read_text()) == expected, rel
        else:
            assert src.read_bytes() == (dst / rel).read_bytes()
    actual = hashes(dst)
    del actual['release_manifest.json']
    assert manifest['files'] == actual and manifest['objects'] == count
    assert set(actual) == set(hashes(modified / 'ckm-staging'))
    renderer = runpy.run_path(str(repo / 'render_ckm.py'))
    stamp = renderer['stamp']('registry-json', 'module:M-CORE', '2.0.0-alpha', str(dst))
    assert stamp['release_cut'] == manifest['cut']
    print('PASS: existing manifest reader accepts technical scope without ratified_by')
    print(f'PASS: real staging: {count} objects, {len(actual)} files; all source metadata preserved; hashes and count valid; staging and ledger unchanged')
    before = hashes(modified)
    result = run(script, modified, '--acknowledge-technical-only')
    assert result.returncode == 1 and 'REFUSED' in result.stdout and hashes(modified) == before
    print('PASS: existing destination is protected against overwrite')
    synthetic = root / 'synthetic'
    (synthetic / 'ckm-staging').mkdir(parents=True)
    (synthetic / 'ckm').mkdir()
    (synthetic / 'ckm' / 'active-only.yaml').write_text('id: ACTIVE-ONLY\n')
    (synthetic / 'ckm-staging' / 'note.txt').write_text('technical fixture\n')
    records = [{'id': 'PENDING', 'status': 'proposed'}, {'id': 'ABSENT'},
               {'id': 'EXISTING', 'status': 'published', 'ratified_by': 'UFD-001',
                'signed_by': 'Source signer', 'signed_date': '2026-01-01'},
               {'id': 'NULL', 'status': 'proposed', 'ratified_by': None}]
    for i, obj in enumerate(records):
        (synthetic / 'ckm-staging' / f'{i}.yaml').write_text(yaml.safe_dump(obj))
    result = run(script, synthetic, '--acknowledge-technical-only')
    assert result.returncode == 0
    for i, obj in enumerate(records):
        assert yaml.safe_load((synthetic / 'ckm-2.0.0-alpha' / f'{i}.yaml').read_text()) == dict(obj, ckm_release='2.0.0-alpha')
    dst = synthetic / 'ckm-2.0.0-alpha'
    assert not (dst / 'active-only.yaml').exists()
    assert (dst / 'note.txt').read_text() == 'technical fixture\n'
    manifest = json.loads((dst / 'release_manifest.json').read_text())
    actual = hashes(dst)
    del actual['release_manifest.json']
    assert manifest['files'] == actual and manifest['objects'] == len(records)
    assert 'ratified_by' not in manifest
    print('PASS: pending, absent, and pre-existing authority fields preserved; absent ledger never represented as verified')
print('ALL CHECKS PASSED')
