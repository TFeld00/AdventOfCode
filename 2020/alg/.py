d={}

def val(c):
    if c.isdigit():return int(c)
    return d.get(c)

for l in r:
    l=l.split()
    o,*p=l
    if o=='ADD':
        a,b,*_=p
    elif o=='':
        a,*_=p