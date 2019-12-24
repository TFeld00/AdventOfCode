from intcode import *
from Queue import *
import sys

m=[]
with open('22.txt','r')as f:
 for l in f:
  m+=l.rstrip('\n'),


def new(s):
    return s[::-1]
def cut(s,n):
    return s[n:]+s[:n]
def deal(s,n):
    l=len(s)
    r=[0]*l
    for i in xrange(l):
        r[(n*i)%l]=s[i]
    return r


def shuffle(s,m):
    for l in m:
        l=l.split()
        if l[0]=='deal':
            if l[1]=='into':
                s=new(s)
            else:
                s=deal(s,int(l[-1]))
        elif l[0]=='cut':
            s=cut(s,int(l[-1]))
    return s


s=range(10007)
s=shuffle(s,m)

print s.index(2019)
