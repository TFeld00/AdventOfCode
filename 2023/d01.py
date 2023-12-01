DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

n=0
n2=0

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        
        l1=[int(c)for c in l if c.isdigit()]
        n+=10*l1[0]+l1[-1]
        
        x=[]
        for i in range(len(l)):
            for j,v in enumerate('one|two|three|four|five|six|seven|eight|nine'.split('|'),1):
                if l[i:].startswith(v):x+=j,
            if l[i].isdigit():x+=int(l[i]),
        n2+=10*x[0]+x[-1]
   
print(n)
print(n2)

