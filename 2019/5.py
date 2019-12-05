L=[]

with open('5.txt','r')as f:
 for l in f:
  L+=map(int,l.split(','))

def read():
    return 5
def get(m,v):
    if m:
        return v
    return l[v]
def intcode(l):
 i=0
 while i<len(l):
  a=l[i]
  if a==99:return l
  D,C,B=a/10000,a/1000%10,a/100%10
  a=a%100
  if a==1:
    b,c,d=l[i+1:i+4]
    l[d]=get(B,b)+get(C,c)
    i+=4
  elif a==2:
    b,c,d=l[i+1:i+4]
    l[d]=get(B,b)*get(C,c)
    i+=4
  elif a==3:
    b=l[i+1]
    l[b]=read()
    i+=2
  elif a==4:
    b=l[i+1]
    print get(B,b)
    i+=2
  elif a==5:
    b,c=l[i+1:i+3]
    if get(B,b):
        i=get(C,c)
    else:i+=3
  elif a==6:
    b,c=l[i+1:i+3]
    if not get(B,b):
        i=get(C,c)
    else:i+=3
  elif a==7:
    b,c,d=l[i+1:i+4]
    l[d]=int( get(B,b)<get(C,c))
    i+=4
  elif a==8:
    b,c,d=l[i+1:i+4]
    l[d]=int( get(B,b)==get(C,c))
    i+=4
  
  else:return 
  
l=L[:]
intcode(l)
print
#print l
