DAY,_,_=__file__.rpartition('.')


from alg.file import download_input
download_input(DAY)

t=''

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        t+=l
        
s=0
l=[]
f=0
for i,c in enumerate(t):
   f^=1
   if f:
      l+=[i//2]*int(c)
   else:
       l+=[-1]*int(c)

i=0
while i<len(l):
    c=l[i]
    if c<0:
        while l[-1]<0:l.pop()
        if i>=len(l):break
        l[i]=l.pop()
    
    s+=i*l[i]
    i+=1
print(s)

# Part 2

l=[]
f=0
for i,c in enumerate(t):
    f^=1
    i//=2
    c=int(c)
    if c:
        if f:
            l+=[c,i],
        else:
            l+=[c,-1],

j=len(l)-1
while j>0:
    c,i = l[j]
    if i<0:j-=1;continue
    for v,(a,b) in enumerate(l[:j]):
        if b<0 and a>=c:
            l[j]=[c,-1]
            r=[[c,i]]
            if a>c:r+=[[a-c,-1]];j+=1
            l[v:v+1]=r
            while j>0 and j<len(l) and l[j-1][1]<0 and l[j][1]<0: # combine empty
                l[j-1][0]+=l[j][0]
                l.pop(j)
            break
    j-=1

s=0
w=0
for c,i in l:
    if i>=0:
        for j in range(w,w+c):
            s+=i*j
    w+=c
print(s)