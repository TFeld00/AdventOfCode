from Queue import *

d={}
e={}
s=set()
with open('6.txt','r')as F:
    for l in F:
        a,b=l.strip().split(')')
        d[b]=a
        s|={b}
        e[b]=e.get(b,[])+[a]

        e[a]=e.get(a,[])+[b]

D={}
def o(b):
    if b not in d:return 0
    if b not in D:
        D[b]=o(d[b])+1
    return D[b]

t=0
while s:
    b=s.pop()
    t+=o(b)
print t

ST=e['YOU'][0]
END=e['SAN'][0]
q=Queue()
q.put((ST,0))
s={ST}
while not q.empty():
 n,l=q.get()
 if n==END:print l;break
 for x in e[n]:
  if x in s:continue
  s|={x}
  q.put((x,l+1))
