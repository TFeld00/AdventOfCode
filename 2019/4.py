from itertools import *

a,b='171309','643603'


n1=0
n2=0
for c in combinations_with_replacement('123456789',6):
    X=''.join(c)
    if X<a:continue
    if X>b:break
    if any(q*2 in X for q in'123456789'):n1+=1
    if any(q*2 in X and q*3 not in X for q in'123456789'):n2+=1

print n1
print n2
