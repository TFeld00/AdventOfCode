L=[]

s1=0
s2=0

def f(n,r=0):
    a=max(0,n/3-2)
    if r and a:
        return a+f(a,1)
    return a

with open('1.txt','r')as F:
    for l in F:
        i=int(l)
        s1+=f(i)
        s2+=f(i,1)

print s1
print s2
