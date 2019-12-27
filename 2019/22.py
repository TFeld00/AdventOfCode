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

#part 2
#copied from:
# https://topaz.github.io/paste/#XQAAAQAgBQAAAAAAAAAzHIoib6pENkSmUIKIED8dy140D1lKWSMhNhZz+hjKgIgfJKPuwdqIBP14lxcYH/qI+6TyUGZUnsGhS4MQYaEtf9B1X3qIIO2JSejFjoJr8N1aCyeeRSnm53tWsBtER8F61O2YFrnp7zwG7y303D8WR4V0eGFqtDhF/vcF1cQdZLdxi/WhfyXZuWC+hs8WQCBmEtuId6/G0PeMA1Fr78xXt96Um/CIiLCievFE2XuRMAcBDB5We73jvDO95Cjg0CF2xgF4yt3v4RB9hmxa+gmt6t7wRI4vUIGoD8kX2k65BtmhZ7zSZk1Hh5p1obGZ6nuuFIHS7FpuSuv1faQW/FuXlcVmhJipxi37mvPNnroYrDM3PFeMw/2THdpUwlNQj0EDsslC7eSncZQPVBhPAHfYojh/LlqSf4DrfsM926hSS9Fdjarb9xBYjByQpAxLDcmDCMRFH5hkmLYTYDVguXbOCHcY+TFbl+G/37emZRFh/d+SkeGqbFSf64HJToM2I7N2zMrWP7NDDY5FWehD5gzKsJpEg34+sG7x2O82wO39qBlYHcYg1Gz4cLBrH1K1P+KWvEdcdj/NBtrl6yftMlCu6pH4WTGUe9oidaiRuQZOGtw71QsTQUuhpdoWO4mEH0U9+CiPZCZLaQolFDSky1J9nDhZZHy3+ETcUeDOfSu+HI3WuKC0AtIRPdG8B9GhtxZQKAx+5kyi/ek7A2JAY9SjrTuvRADxx5AikbHWXIsegZQkupAc2msammSkwY8dRMk0ilf5vh6kR0jHNbSi0g0KJLCJfqggeX24fKk5Mdh8ULZXnMfMZOmwEGfegByYbu91faLijfW4hoXCB1nlsWTPZEw2PCZqqhl9oc1q25H2YkkvKLxEZWl6a9eFuRzxhB840I1zdBjUVgfKd9/V4VdodzU2Z2e+VEh7RbJjQNFC/rG8dg==
n = 119315717514047
c = 2020

a, b = 1, 0
for l in m:
    l=l.split()
    if l[0]=='deal':
        if l[1]=='into':
            la, lb = -1, -1
        else:
            la, lb = int(l[-1]), 0
    elif l[0]=='cut':
        la, lb = 1, -int(l[-1])
    a = (la * a) % n
    b = (la * b + lb) % n

M = 101741582076661

def inv(a, n): return pow(a, n-2, n)

Ma = pow(a, M, n)
Mb = (b * (Ma - 1) * inv(a-1, n)) % n

print(((c - Mb) * inv(Ma, n)) % n)
