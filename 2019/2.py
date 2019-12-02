L=[]

with open('2.txt','r')as f:
 for l in f:
  L+=map(int,l.split(','))

def intcode(l):
 i=0
 while i<len(l):
  a=l[i]
  if a==99:return l
  b,c,d=l[i+1:i+4]
  if a==1:
    l[d]=l[b]+l[c]
    i+=4
  elif a==2:
    l[d]=l[b]*l[c]
    i+=4
  else:return
  
l=L[:]
l[1]=12
l[2]=2
print intcode(l)[0]

for q in range(100):
 for w in range(100):
  l=L[:]
  
  l[1]=q
  l[2]=w
  l=intcode(l)
  if l and l[0]==19690720:
   print 100*q+w
   1/0 #BREAK!
