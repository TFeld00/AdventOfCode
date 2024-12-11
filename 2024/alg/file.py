from datetime import datetime
import os
import requests

YEAR = 2024

def download_input(day_file):
    file = day_file+'.txt'
    day = int(day_file[-2:])

    if os.path.exists(file) and os.path.getsize(file) > 0:
        return
    
    url=f'https://adventofcode.com/{YEAR}/day/{day}/input'
    session='53616c7465645f5fb1063f681deefc22fb1d87299e9d028ffb85016377769673c66aa3e2fe44b6919e38635d547b5056adf4d4baab8f63844867058c16e4b64f'
    r=requests.get(url,cookies={'session':session})
    if r.status_code == 404:
        return

    with open(file,'w')as F:
        F.writelines(r.text)
