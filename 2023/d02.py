DAY,_,_=__file__.rpartition('.')

COLS = {
    '.': (255, 255, 255),
    '#': (0, 0, 0),
}

from alg.file import download_input
download_input(DAY)

r,g,b=12,13,14
s=0
i=0
PS=0

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        i+=1
        a,b=l.split(':')
        b=b.split(';')
        valid = 1
        R=G=B=0
        for v in b:
            for x in v.split(','):
                a,b=x.split()
                a=int(a)
                if b[0]=='r':
                    R=max(R,a)
                if b[0]=='g':
                    G=max(G,a)
                if b[0]=='b':
                    B=max(B,a)
        PS+=R*G*B
        if R<=12 and G<=13 and B<=14:s+=i

print(s)
print(PS)