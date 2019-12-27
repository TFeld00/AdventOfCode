from intcode import *
from Queue import *
import sys

L=[]
with open('25.txt','r')as f:
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

commands="""east
take asterisk
north
north
take hypercube
north
take coin
north
take easter egg
south
south
south
south
west
west
take fixed point
north
take sand
south
east
east
north
west
north
take spool of cat6
north
take shell
west
drop sand
drop hypercube
drop fixed point
drop easter egg
drop shell
drop asterisk
drop spool of cat6
drop coin
take fixed point
take sand
take coin
take spool of cat6
north
inv
"""
q=map(ord,commands)
q=q[::-1]
def read():
    global q
    return q.pop()
i=0
intcode(mem,read,write)


