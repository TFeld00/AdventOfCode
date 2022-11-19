DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

s=''

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        s=l

s=[ord(c)%32-1 for c in s]
n=0
for d in s:
    n=n*26+d

def g(n):
    s=[]
    while n:
        s=[n%26]+s
        n//=26
    return s

def f(n):
    s=g(n)
    v=w=0
    for i in range(len(s)-1):
        if i<len(s)-2:
            a,b,c=s[i:i+3]
            if a+1==b==c-1:v=1;break
        a,b=s[i:i+2]
        if a==b:w+=1
    if not v:return 0
    if w<2:return 0
    if any(ord(x)-97 in s for x in 'iol'):return 0
    return 1

def h(s):
    return ''.join(chr(d+97)for d in s)

#part 1
n+=1
while not f(n):n+=1
print(h(g(n)))

#part 2
n+=1
while not f(n):n+=1
print(h(g(n)))