from datetime import datetime
import os
import requests

YEAR = 2023

def download_input(day_file):
    file = day_file+'.txt'
    day = int(day_file[-2:])

    if os.path.exists(file) and os.path.getsize(file) > 0:
        return
    
    url=f'https://adventofcode.com/{YEAR}/day/{day}/input'
    session='53616c7465645f5fda354baf43adc5e7edb1f41e4d68525916e1c47a3c4bcd0ee1fc7993708fecc3618fe9bd41d021ba3e762cb60c1acaed1bd4a90a3ee48332'
    r=requests.get(url,cookies={'session':session})
    if r.status_code == 404:
        return

    with open(file,'w')as F:
        F.writelines(r.text)
