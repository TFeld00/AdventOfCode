DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]
with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

s=0
for l in r:
    x=len(l)//2
    v={*l[:x]}&{*l[x:]}
    v=v.pop()
    s+=ord(v)%32 + 26*v.isupper()
print(s)


s=0
for i in range(0,len(r),3):
    a,b,c=r[i:i+3]
    v={*a}&{*b}&{*c}
    v=v.pop()
    s+=ord(v)%32 + 26*v.isupper()
print(s)