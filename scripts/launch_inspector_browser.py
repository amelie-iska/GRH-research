#!/usr/bin/env python3
"""Start the existing local Chrome/CDP harness in a preserved isolated profile."""
from pathlib import Path
import datetime
import json
import socket
import subprocess

ROOT=Path(__file__).resolve().parents[1]
CHROME=Path('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')


def main():
    if not CHROME.is_file():raise SystemExit('Existing Google Chrome executable unavailable; no installation attempted.')
    with socket.socket() as s:
        if s.connect_ex(('127.0.0.1',9242))==0:
            raise SystemExit('Port9242 is already in use; do not replace or close an unrelated browser.')
    folder=ROOT/'outputs/browser-tests/2026-11-03-inspector'
    folder.mkdir(parents=True,exist_ok=True)
    profile=folder/('profile-'+datetime.datetime.now().strftime('%H%M%S%f'))
    with (folder/'chrome.log').open('ab') as log:
        process=subprocess.Popen([str(CHROME),'--headless=new','--remote-debugging-port=9242',
            '--remote-debugging-address=127.0.0.1','--no-first-run','--no-default-browser-check',
            '--disable-background-networking','--user-data-dir='+str(profile),'about:blank'],
            stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
    record=dict(pid=process.pid,profile=str(profile),task='architecture-inspector-headless-test')
    (folder/('process-'+str(process.pid)+'.json')).write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,indent=2))


if __name__=='__main__':main()
