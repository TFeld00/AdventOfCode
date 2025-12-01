from datetime import datetime
import os
import requests

YEAR = 2025

def download_input(day_file):
    file = day_file+'.txt'
    day = int(day_file[-2:])

    if os.path.exists(file) and os.path.getsize(file) > 0:
        return
    
    url=f'https://adventofcode.com/{YEAR}/day/{day}/input'
    session='53616c7465645f5f521d6846b0cdebdcd43266822ce8bec9aa1beb12c7ce68e20035d778441ff5b91d179ac0e23c6f743d3d8f6aa96f0d93b47577b4a4afec36'
    r=requests.get(url,cookies={'session':session})
    if r.status_code == 404:
        return

    with open(file,'w')as F:
        F.writelines(r.text)
