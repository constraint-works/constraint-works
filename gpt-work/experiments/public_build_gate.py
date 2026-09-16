#!/usr/bin/env python3
"""Bounded public source-build screen. No patching, publishing or credentials.
Run with --python pointing to an isolated Python 3.14 environment with pip.
Downloads public source archives, verifies PyPI hashes and executes build backends.
Only run in a disposable environment. Results are not functional certification.
"""
import argparse, concurrent.futures, datetime, hashlib, json, os, pathlib
import subprocess, time, urllib.request
from packaging.version import Version, InvalidVersion

ROOT = pathlib.Path(__file__).resolve().parents[1]

def get_json(url):
    with urllib.request.urlopen(url, timeout=20) as r:
        return json.load(r)

def run_case(case, python, work):
    out = dict(case)
    started = time.monotonic()
    try:
        meta = get_json('https://pypi.org/pypi/' + case['name'] + '/json')
        out['metadata_url'] = 'https://pypi.org/pypi/' + case['name'] + '/json'
        out['current_latest_version'] = meta['info']['version']
        if 'version' in case:
            version = case['version']
        else:
            matches = []
            for v, artifacts in meta['releases'].items():
                try:
                    parsed = Version(v)
                except InvalidVersion:
                    continue
                if parsed.is_prerelease or parsed.is_devrelease:
                    continue
                if any(a['upload_time_iso_8601'].startswith(case['recorded_last_release']) for a in artifacts):
                    matches.append(parsed)
            if not matches:
                out.update(status='NO_MATCHING_RECORDED_RELEASE')
                return out
            version = str(max(matches))
        out['version'] = version
        artifacts = [a for a in meta['releases'][version] if a['packagetype'] == 'sdist' and not a['yanked']]
        if not artifacts:
            out.update(status='NO_SDIST')
            return out
        artifact = sorted(artifacts, key=lambda a: a['filename'])[0]
        out.update(sdist_url=artifact['url'], sdist_sha256=artifact['digests']['sha256'], upload_time=artifact['upload_time_iso_8601'])
        folder = work / case['name']
        folder.mkdir(parents=True, exist_ok=True)
        archive = folder / pathlib.Path(artifact['filename']).name
        with urllib.request.urlopen(artifact['url'], timeout=30) as response:
            content = response.read(20_000_001)
        if len(content)>20_000_000:
            raise ValueError('Archive exceeds experiment size limit')
        if hashlib.sha256(content).hexdigest() != out['sdist_sha256']:
            raise ValueError('PyPI digest mismatch')
        archive.write_bytes(content)
        command = [python, '-m', 'pip', '--disable-pip-version-check', 'wheel', '--no-deps', '--no-cache-dir', '--progress-bar', 'off', '--wheel-dir', str(folder/'wheels'), str(archive)]
        env = {k:v for k,v in os.environ.items() if k in {'PATH','HOME','TMPDIR','SSL_CERT_FILE','SSL_CERT_DIR','HTTPS_PROXY','HTTP_PROXY','NO_PROXY'}}
        env.update(PIP_INDEX_URL='https://pypi.org/simple', PIP_DEFAULT_TIMEOUT='25', PIP_RETRIES='1')
        run = subprocess.run(command, cwd=folder, env=env, capture_output=True, text=True, timeout=120)
        log = run.stdout + '\n' + run.stderr
        (folder/'build.log').write_text(log)
        out.update(status='BUILT' if run.returncode == 0 else 'BUILD_FAILED_REQUIRES_CLASSIFICATION', returncode=run.returncode,
                   log_sha256=hashlib.sha256(log.encode()).hexdigest(), log_tail=log[-5000:])
    except subprocess.TimeoutExpired:
        out['status']='BUILD_TIMEOUT'
    except Exception as e:
        out.update(status='FETCH_OR_INFRA_ERROR',error=type(e).__name__+': '+str(e))
    finally:
        out['elapsed_seconds']=round(time.monotonic()-started,2)
    return out

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--python',required=True)
    parser.add_argument('--work-dir',required=True)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    protocol_path=ROOT/'data/public-build-protocol.json'
    protocol_bytes=protocol_path.read_bytes()
    protocol=json.loads(protocol_bytes)
    work=pathlib.Path(args.work_dir).resolve();work.mkdir(parents=True,exist_ok=True)
    cases=[dict(c,role='UNSEEN_BUILD_SCREEN') for c in protocol['sample']]
    cases.append(dict(protocol['known_control'],role='KNOWN_POSITIVE_CONTROL'))
    results=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        future_map={pool.submit(run_case,c,args.python,work):c for c in cases}
        for future in concurrent.futures.as_completed(future_map):
            result=future.result();results.append(result)
            print(result['name'],result['status'],result.get('version',''),flush=True)
    results.sort(key=lambda r:r.get('rank',9999))
    report=dict(date_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                protocol_sha256=hashlib.sha256(protocol_bytes).hexdigest(),
                python=subprocess.check_output([args.python,'--version'],text=True).strip(),
                pip=subprocess.check_output([args.python,'-m','pip','--version'],text=True).strip(),
                interpretation='Build-only prerequisite screen; no inference about functional correctness, revenue or AI A/B effect.',results=results)
    pathlib.Path(args.output).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')

if __name__=='__main__':main()
