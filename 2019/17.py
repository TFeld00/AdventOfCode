from intcode import *
from Queue import *
import sys

L=[]
with open('17.txt','r')as f:
 for l in f:
  L+=map(int,l.split(','))

m=['']

def write(s):
    global m
    c=chr(s)
    if c!='\n':m[-1]+=c
    else:m+='',

l=dict(enumerate(L))
i=0
while 1:
    r=intcodeUntilRead(l,i,read,write)
    if not r:break
    l,i=r

t=0
#for l in m:
#    print l
    
m=[l for l in m if l]
for i,l in enumerate(m):
    for j,c in enumerate(l):
        if c=='#':
            if len(m[i])-1>j>0<i<len(m)-1:
                if m[i-1][j]==m[i+1][j]==m[i][j-1]==m[i][j+1]==c:
                    t+=i*j
print t

mem=dict(enumerate(L))
mem[0]=2
m=''

def write2(s):
    if s>255:print s;return
    global m
    c=chr(s)
    if c!='\n':m+=c
    else:
        print m
        m=''

commands="""A,B,B,A,C,A,C,A,C,B
L,6,R,12,R,8
R,8,R,12,L,12
R,12,L,12,L,4,L,4
n
"""
q=map(ord,commands)
q=q[::-1]
def read():
    global q
    return q.pop()
i=0
while 1:
    r=intcodeUntilRead(mem,i,read,write2)
    if not r:break
    mem,i=r
