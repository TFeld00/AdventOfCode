import re
G=[]
S=0
BOOST=33
with open('24.txt','r')as f:
 for l in f:
  if l[:2]=='Im':S=1
  elif l[:2]=='In':S=2
  elif l=='\n':pass
  else:
   x=l.split()
   u=int(x[0])
   hp=int(x[4])
   wi=' '.join(x[7:-11])[1:-1].split('; ')
   w,im=[],[]
   for _ in wi:
    if _[:4]=='weak':w=_[8:].split(', ')
    if _[:4]=='immu':im=_[10:].split(', ')
   d=int(x[-6])
   t=x[-5]
   i=int(x[-1])
   A={'type':S,'units':u,'hp':hp,'weak':w,'immune':im,'dmg':d,'dmgType':t,'init':i}
   if A['type']==1:A['dmg']+=BOOST
   G+=[A]


for _ in range(50000):
 ATK=sorted(G,key=lambda A:(A['units']*A['dmg'],A['init']),reverse=True)
 #sel
 targets=[]
 for g in ATK:
  weak=[_ for _ in G if _['type']!=g['type'] and g['dmgType']in _['weak']and _ not in targets]
  weak=sorted(weak,key=lambda g:(g['units']*g['dmg'],g['init']))
  if weak:
   g['target']=weak[-1]
   targets+=[weak[-1]]
   continue
  norm=[_ for _ in G if _['type']!=g['type'] and g['dmgType']not in _['weak']+_['immune']and _ not in targets]
  norm=sorted(norm,key=lambda g:(g['units']*g['dmg'],g['init']))
  if norm:
   g['target']=norm[-1]
   targets+=[norm[-1]]
  else:g['target']=None

 #atk
 dead=[]
 ATK=sorted(ATK,key=lambda g:g['init'],reverse=True)
 for g in ATK:
  if g in dead:continue
  if g['units']<=0:dead+=[g];continue
  t=g['target']
  if not t:continue
  D=1
  if g['dmgType']in t['weak']:
   D=2
  D*=(g['units']*g['dmg'])
  U=D//t['hp']
  t['units']-=U
  if t['units']<=0:dead+=[t]

 #check
 G=[g for g in ATK if g not in dead]
 A=sum(g['units']for g in G if g['type']==1)
 B=sum(g['units']for g in G if g['type']==2)
 if A==0 or B==0:
  print A,B
  break
print [g['units']for g in G if g['type']==1]
print [g['units']for g in G if g['type']==2]
