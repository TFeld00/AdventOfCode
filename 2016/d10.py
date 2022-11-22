DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split()
        r+=[l]

I={}
B={}
O={}
s=set()
for o,*l in r:
    if o=='value':
        v,*_,b = l
        b=int(b)
        B[b]=B.get(b,[])+[int(v)]
        if len(B[b])>1:s|={b}
    else:
        b,_,_,_,ol,vl,_,_,_,oh,vh=l
        b=int(b)
        I[b]=I.get(b,[])+[(ol=='bot',int(vl),oh=='bot',int(vh))]

while s:
    b=s.pop()
    x,y=sorted(B[b])
    if (x,y)==(17,61):print(b) #part 1
    B[b]=[]
    ol,vl,oh,vh=I[b][0]
    if ol:
        B[vl]=B.get(vl,[])+[x]
        if len(B[vl])>1:s|={vl}
    else:
        O[vl]=O.get(vl,[])+[x]
    if oh:
        B[vh]=B.get(vh,[])+[y]
        if len(B[vh])>1:s|={vh}
    else:
        O[vh]=O.get(vh,[])+[y]

#part 2
print(O[0][0] * O[1][0] * O[2][0])