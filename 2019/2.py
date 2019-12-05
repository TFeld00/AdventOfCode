from intcode import *

L=[]
with open('2.txt','r')as f:
 for l in f:
  L+=map(int,l.split(','))

  
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


