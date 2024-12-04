DAY,_,_=__file__.rpartition('.')

from alg.util import rotate90clockwise, rotate180, rotate90counterclockwise
from alg.file import download_input
from alg.grid import word_search, pattern_search

download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]
        
W,H=len(r[0]),len(r)
        
# Part 1
print(word_search(r, 'XMAS', includeDiagonals=True))

# Part 2
pattern="""M.S
.A.
M.S"""
print(pattern_search(r, pattern, rotate=True))