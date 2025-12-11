DAY,_,_=__file__.rpartition('.')

from functools import cache

from alg.file import download_input
download_input(DAY)

d={}
with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        a,*l=l.split()
        a=a[:-1]
        d[a]=l

@cache
def f(n,t,*x):
    if n in x:return 0
    if n==t:
        return 1
    return sum(f(v,t,*x)for v in d.get(n,[]))

# Part 1
print(f('you','out'))

# Part 2
a=f('svr','dac','fft','out')*f('dac','fft','out')*f('fft','out','dac')
b=f('svr','fft','dac','out')*f('fft','dac','out')*f('dac','out','fft')
print(a+b)