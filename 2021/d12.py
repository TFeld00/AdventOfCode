DAY,_,_=__file__.rpartition('.')

from queue import *

from alg.file import download_input
download_input(DAY)

r=[]
s=0

e={}

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        a,b=l.split('-')
        e[a]=e.get(a,[])+[b]
        e[b]=e.get(b,[])+[a]
        pass

q=Queue()
s=set()
q.put(('start',set()))
r=0
while not q.empty():
    n,small=q.get()
    for v in e.get(n):
        if v=='end':r+=1
        elif v.islower() and v in small:continue
        else:
            q.put((v,small|{n}))
print(r)

q=Queue()
s=set()
q.put(('start',set(),None,['start']))
r=0
while not q.empty():
    n,small,double,p=q.get()
    for v in e.get(n,[]):
        x=double
        if v=='start':continue
        elif v=='end':r+=1;continue
        elif v.islower() and v in small:
            if x is None:x=v
            else:continue
        q.put((v,small|{v},x,p+[v]))
print(r)
