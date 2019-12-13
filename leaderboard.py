from datetime import *
A=''
with open('leaderboard.txt','r')as f:
    for l in f:A+=l
a=eval(A)

print a['event']
mem=a['members']
for id in sorted(mem,key=lambda id:mem[id]['local_score'],reverse=True):
 m=mem[id]
 print m['local_score'],'\t',m['name']
 com=m['completion_day_level']
 for c in sorted(com,key=int):
  print '\t','%2d'%int(c),
  d=[]
  for s in com[c]:
   d+=[datetime.fromtimestamp(int(com[c][s]['get_star_ts']))]
   print '\t',str(d[-1])[5:],
  if len(d)==2:
   print '\t',d[1]-d[0]
  else:
   print
