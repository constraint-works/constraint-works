#!/usr/bin/env python3
"""Koe 06, R7: lukee tallennettujen testiviestien (.eml) Authentication-Results-otsakkeet ja
raportoi SPF/DKIM/DMARC-tuloksen. Ei tulosta osoitteita eikä verkkotunnuksia (repo on julkinen).
Käyttö: python3 kokeet/06-r7-otsaketarkistin.py polku/*.eml"""
import sys, re, email, email.policy
def tarkista(p):
    msg=email.message_from_binary_file(open(p,"rb"),policy=email.policy.default)
    ar=" ".join(str(h) for h in msg.get_all("Authentication-Results",[]))+" "+" ".join(str(h) for h in msg.get_all("ARC-Authentication-Results",[]))
    res={}
    for k in ("spf","dkim","dmarc"):
        m=re.search(rf"\b{k}=(\w+)",ar,re.I); res[k]=m.group(1).lower() if m else "puuttuu"
    vastaanottaja=re.search(r"^\s*([\w.-]+);",ar)
    palvelu=vastaanottaja.group(1).split(".")[-2] if vastaanottaja and "." in vastaanottaja.group(1) else "tuntematon"
    roska=any("spam" in str(msg.get(h,"")).lower() or str(msg.get(h,"")).strip().upper()=="YES" for h in ("X-Spam-Flag","X-Spam-Status"))
    return palvelu,res,roska
if __name__=="__main__":
    ok=True
    for p in sys.argv[1:]:
        palvelu,res,roska=tarkista(p)
        rivi=f"vastaanottava palvelu={palvelu} spf={res['spf']} dkim={res['dkim']} dmarc={res['dmarc']} roskapostiotsake={'kyllä' if roska else 'ei'}"
        print(rivi)
        ok &= all(v=="pass" for v in res.values()) and not roska
    print("R7 OTSAKKEET:", "PASS" if ok and len(sys.argv)>1 else "EI LÄPI tai ei tiedostoja")
