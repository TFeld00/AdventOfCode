from string import ascii_lowercase, ascii_uppercase
def shift_caesar(s,n):
    a=ascii_lowercase + ascii_uppercase
    b=ascii_lowercase[n%26:]+ascii_lowercase[n%26:] + ascii_uppercase[n%26:]+ascii_uppercase[n%26:]
    t=str.maketrans(a,b)
    
    return s.translate(t)

def tr(s,a,b):
    t=str.maketrans(a,b)
    return s.translate(t)