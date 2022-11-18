from datetime import datetime
import os
import requests

YEAR = 2022

def download_input(day_file):
    file = day_file+'.txt'
    day = int(day_file[-2:])

    if os.path.exists(file) and os.path.getsize(file) > 0:
        return
    
    url=f'https://adventofcode.com/{YEAR}/day/{day}/input'
    session='53616c7465645f5f4acbc93133b77f8dc4bd3d50c720207edf02a2731c511d2a44f759ea2e016465f4cffaf59a213566e1db3fa3c780202a571d5e35ebee85b6'
    r=requests.get(url,cookies={'session':session})
    if r.status_code == 404:
        return

    with open(file,'w')as F:
        F.writelines(r.text)
