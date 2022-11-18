DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]
s=0

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,l.split('x'))]
        r+=[l]

#part 1
print(sum(2*l*w + 2*w*h + 2*h*l + min(l*w,w*h,h*l) for l,w,h in r))

#part 2
print(sum(2*min(l+w,w+h,h+l)+l*w*h for l,w,h in r))
