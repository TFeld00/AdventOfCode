def parse_with_headers(F):
    d={}
    n=''
    r=[]
    for l in F:
        if not l:
            d[n]=r
            n=''
            r=[]
        elif l and not n:n=l
        elif n:
            r+=[l]
    if r:d[n]=r
    return d

def parse_no_headers(F):
    d=[]
    r=[]
    for l in F:
        if not l:
            d+=[r]
            r=[]
        else:
            r+=[l]
    if r:d+=[r]
    return d


def parse_skip_headers(F):
    d=[]
    r=[]
    n=''
    for l in F:
        if not l:
            d+=[r]
            n=''
            r=[]
        elif l and not n:n=l
        elif n:
            r+=[l]
    if r:d+=[r]
    return d