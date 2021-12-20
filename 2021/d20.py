from alg.file import download_input
from alg.cellular import step_dict, to_dict
from alg.util import parse_no_headers
DAY, _, _ = __file__.rpartition('.')

download_input(DAY)

r = []
s = 0

with open(f'{DAY}.txt', 'r')as F:
    for l in F:
        l = l.rstrip('\n')
        r += [l]

e, r = parse_no_headers(r)

e = e[0]


d = to_dict(r, lambda v: int(v == '#'))
m=[[int(v == '#')for v in l]for l in r]

def enhance(n):
    s = 0
    for v in n:
        s *= 2
        s += v
    return int(e[s] == '#')

default = 0

for _ in range(50):
    d = step_dict(d, enhance, default)
    default = int(e[int(str(default)*9, 2)] == '#')
    if _ in (1, 49):    
        print(sum(d.values()))