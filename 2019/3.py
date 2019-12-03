d1={}
d2={}
I={}
T=0
with open('3.txt','r')as F:
    for l in F:
        x,y=0,0
        t=0
        for m in l.split(','):
            d,w=m[0],int(m[1:])
            for i in range(1,w+1):
                if d=='L':x-=1
                elif d=='U':y-=1
                elif d=='R':x+=1
                elif d=='D':y+=1
                if T:
                    d2[(x,y)]=1
                    if(x,y)in d1:
                        I[(x,y)]=I.get((x,y),[])+[(t+i+d1[(x,y)])]
                else:
                    d1[(x,y)]=t+i
            t+=i
        T=1
print min(abs(x)+abs(y)for x,y in I.keys())
print min(I.values())
