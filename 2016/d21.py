DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split()
        r+=[l]


def f(p,dir=1):
    p=list(p)
    for o,*l in r[::dir]:
        if o=='swap':
            a,x,_,b,y=l
            if a=='position':
                i=int(x)
                j=int(y)
            else:
                i=p.index(x)
                j=p.index(y)
            p[i],p[j]=p[j],p[i]
        elif o=='rotate':
            d,*_=l
            if d=='based':
                if dir>0:
                    i=p.index(l[-1])
                    i+=i>3
                    i+=1
                    i%=len(p)
                    p=p[-i:]+p[:-i]
                else:
                    i=0
                    while 1:
                        p=p[1:]+p[:1]
                        if p[i-(i>4)]==l[-1]:break
                        i+=1

            else:
                i=int(_[0])
                i*=[-1,1][d=='right']
                i*=dir
                p=p[-i:]+p[:-i]
        elif o=='reverse':
            _,x,_,y=l
            i=int(x)
            j=int(y)
            p[i:j+1] = p[i:j+1][::-1]
        elif o=='move':
            _,x,*_,y=l
            i=int(x)
            j=int(y)
            if dir<0:i,j=j,i
            v=p.pop(i)
            p.insert(j,v)

    return''.join(p)

#part 1
print(f('abcdefgh'))
#part 2
print(f('fbgdceah',-1))