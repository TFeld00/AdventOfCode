from datetime import datetime
import os
import requests

YEAR = 2021

def download_input(day_file):
    file = day_file+'.txt'
    day = int(day_file[-2:])

    if os.path.exists(file) and os.path.getsize(file) > 0:
        return
    
    url=f'https://adventofcode.com/{YEAR}/day/{day}/input'
    session='53616c7465645f5f33df4ab6c37a0b8243cea5ab8dbfe729cdc27a47f9c5fdc0781b47155f2f2ecb89d32fdae64f6971'
    r=requests.get(url,cookies={'session':session})

    with open(file,'w')as F:
        F.writelines(r.text)
