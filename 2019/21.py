from intcode import *
from Queue import *
import sys

L=[]
with open('21.txt','r')as f:
 for l in f:
  L+=map(int,l.split(','))


mem=dict(enumerate(L))
m=''

def write(s):
    if s>255:print s;return
    global m
    c=chr(s)
    if c!='\n':m+=c
    else:
        print m
        m=''

commands="""NOT A J
NOT B T
OR T J
NOT C T
OR T J
AND D J
WALK
"""
q=map(ord,commands)
q=q[::-1]
def read():
    global q
    return q.pop()
i=0
while 1:
    r=intcodeUntilRead(mem,i,read,write)
    if not r:break
    mem,i=r



mem=dict(enumerate(L))
m=''

commands="""NOT A J
NOT B T
OR T J
NOT C T
OR T J
AND D J
NOT E T
AND H T
OR E T
AND T J
RUN
"""
q=map(ord,commands)
q=q[::-1]
i=0
while 1:
    r=intcodeUntilRead(mem,i,read,write)
    if not r:break
    mem,i=r
