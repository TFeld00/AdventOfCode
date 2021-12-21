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
    session='53616c7465645f5fe59bc9f3877e3d25802b9a8376955dca2936d1e475172da12ed11dc72fae248bea7f58958c01106c'
    r=requests.get(url,cookies={'session':session})
    if r.status_code == 404:
        return

    with open(file,'w')as F:
        F.writelines(r.text)
