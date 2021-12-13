DAY,_,_=__file__.rpartition('.')

from img.img import write_img_fromlist     #write_img(DAY,COLS)
from alg.util import parse_no_headers

from alg.file import download_input
download_input(DAY)

r=[]
s=0

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

a,b = parse_no_headers(r)

s=set()
for v in a:
    x,y=map(int,v.split(','))
    s|={(x,y)}

i=0
for f in b:
    S=set()
    c=int(f[13:])
    if f[11]=='x':
        for x,y in s:
            S|={(x if x <=c else -x%c,y)}
    elif f[11]=='y':
        for x,y in s:
            S|={(x,y if y <=c else -y%c)}
    s=S
    if i==0:print(len(s))
    i+=1

m=[['.']*(8*4+7) for _ in' '*6]
for x,y in s:m[y][x]='#'
for l in m:print(*l,sep='')

write_img_fromlist(m,DAY)