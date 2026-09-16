#!/usr/bin/env python3
"""Koe 03 -ajuri. Lukittu protokolla: per rivi 5 min konetta, ei korjausyrityksiä.
Vaihe 1: venv python3.14, pip install --no-binary :all: pkg==latest
Vaihe 2: import
Vaihe 3: pip install pkg (wheel) + import
Kirjaa: vaihe, jossa epäonnistui, virheilmoituksen ensimmäinen rivi (viimeinen 'Error'-rivi stderr:stä)."""
import csv, json, subprocess, sys, time, os, urllib.request, re, shutil
OTOS = "./kokeet/03-otos.csv"
ULOS = "./kokeet/03-tulokset.jsonl"
TYO = "/tmp/eikaisiina-scratch/koe03"
RAJA = 300  # s per rivi

def latest(pkg):
    with urllib.request.urlopen(f"https://pypi.org/pypi/{pkg}/json", timeout=60) as r:
        d = json.load(r)
    return d["info"]["version"]

def run(cmd, deadline, cwd=None, env=None):
    left = max(1, int(deadline - time.time()))
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=left, cwd=cwd, env=env)
        return p.returncode, p.stdout, p.stderr, False
    except subprocess.TimeoutExpired as e:
        return -1, (e.stdout or "") if isinstance(e.stdout, str) else "", (e.stderr or "") if isinstance(e.stderr, str) else "", True

def eka_virherivi(out, err):
    t = (err or "") + "\n" + (out or "")
    lines = [l.strip() for l in t.splitlines() if l.strip()]
    # ensimmäinen rivi, joka sisältää Error/error/Exception/failed
    for l in lines:
        if re.search(r"(Error|Exception|error:|failed|FAILED|No module named|cannot import)", l):
            return l[:300]
    return (lines[-1][:300] if lines else "")

def moduulit(py, pkg):
    code = ("import importlib.metadata as m, json\n"
            "pd=m.packages_distributions()\n"
            f"names=[k for k,v in pd.items() if any(x.lower().replace('_','-')=='{pkg.lower().replace('_','-')}' for x in v)]\n"
            "print(json.dumps(sorted(set(names))))")
    rc, out, err, to = run([py, "-c", code], time.time() + 60)
    try:
        ms = json.loads(out.strip().splitlines()[-1])
    except Exception:
        ms = []
    ms = [x for x in ms if not x.startswith(("test", "_"))] or ms
    return ms or [pkg.replace("-", "_").replace(".", "_")]

def aja_rivi(pkg, versio_pakotettu=None):
    alku = time.time(); deadline = alku + RAJA
    tulos = {"nimi": pkg, "alku": time.strftime("%H:%M:%S")}
    try:
        ver = versio_pakotettu or latest(pkg)
    except Exception as e:
        tulos.update(vaihe="0_pypi_json", tila="virhe", virhe=str(e)[:200]); return tulos
    tulos["versio"] = ver
    vdir = os.path.join(TYO, "venv_" + re.sub(r"[^A-Za-z0-9]", "_", pkg))
    shutil.rmtree(vdir, ignore_errors=True)
    rc, out, err, to = run(["python3.14", "-m", "venv", vdir], deadline)
    py = os.path.join(vdir, "bin", "python")
    env = dict(os.environ, PIP_DISABLE_PIP_VERSION_CHECK="1", PIP_NO_INPUT="1")
    # Vaihe 1: lähdeasennus
    rc, out, err, to = run([py, "-m", "pip", "install", "--no-binary", ":all:", f"{pkg}=={ver}"], deadline, env=env)
    tulos["v1_lahde_rc"] = rc; tulos["v1_timeout"] = to
    if rc != 0:
        tulos.update(vaihe="1_lahdeasennus", tila="epaonnistui", virhe=eka_virherivi(out, err))
    else:
        mods = moduulit(py, pkg); tulos["moduulit"] = mods
        rc2, out2, err2, to2 = run([py, "-c", f"import {mods[0]}"], deadline)
        tulos["v2_import_rc"] = rc2
        if rc2 != 0:
            tulos.update(vaihe="2_import_lahde", tila="epaonnistui", virhe=eka_virherivi(out2, err2))
        else:
            tulos.update(vaihe="2_import_lahde", tila="onnistui")
    # Vaihe 3: wheel-asennus tuoreeseen venviin (vain jos vaiheet 1-2 onnistuivat, protokollan mukaan)
    if tulos.get("tila") == "onnistui":
        vdir2 = vdir + "_wheel"; shutil.rmtree(vdir2, ignore_errors=True)
        run(["python3.14", "-m", "venv", vdir2], deadline); py2 = os.path.join(vdir2, "bin", "python")
        rc3, out3, err3, to3 = run([py2, "-m", "pip", "install", f"{pkg}=={ver}"], deadline, env=env)
        tulos["v3_wheel_rc"] = rc3
        if rc3 != 0:
            tulos.update(vaihe="3_wheel", tila="epaonnistui", virhe=eka_virherivi(out3, err3))
        else:
            mods = tulos.get("moduulit") or moduulit(py2, pkg)
            rc4, out4, err4, to4 = run([py2, "-c", f"import {mods[0]}"], deadline)
            tulos["v3_import_rc"] = rc4
            if rc4 != 0: tulos.update(vaihe="3_import_wheel", tila="epaonnistui", virhe=eka_virherivi(out4, err4))
            else: tulos.update(vaihe="3_import_wheel", tila="onnistui")
        shutil.rmtree(vdir2, ignore_errors=True)
    if time.time() > deadline: tulos["aikaraja_ylittyi"] = True
    tulos["kesto_s"] = round(time.time() - alku, 1)
    shutil.rmtree(vdir, ignore_errors=True)
    return tulos

if __name__ == "__main__":
    rivit = list(csv.DictReader(open(OTOS)))
    with open(ULOS, "w") as f:
        for r in rivit:
            t = aja_rivi(r["nimi"]); t["jarjestys"] = int(r["jarjestys"])
            f.write(json.dumps(t, ensure_ascii=False) + "\n"); f.flush()
            print(r["jarjestys"], r["nimi"], t.get("versio"), t.get("vaihe"), t.get("tila"), t.get("kesto_s"), file=sys.stderr, flush=True)
        # positiivinen kontrolli
        t = aja_rivi("html5lib", "1.1"); t["jarjestys"] = 0; t["kontrolli"] = True
        f.write(json.dumps(t, ensure_ascii=False) + "\n")
        print("kontrolli html5lib 1.1", t.get("vaihe"), t.get("tila"), t.get("virhe"), file=sys.stderr, flush=True)
