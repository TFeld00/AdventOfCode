from datetime import *
import sys

A=''
with open('leaderboard.txt','r')as f:
    for l in f:A+=l
a=eval(A)

days=[datetime(2019,12,i,6)for i in range(1,26)]

sys.stdout.write(a['event']+'\n')
mem=a['members']
best={}

for id in sorted(mem,key=lambda id:mem[id]['local_score'],reverse=True):
 m=mem[id]
 sys.stdout.write('%s\t%s\n'%(m['local_score'],m['name']))
 com=m['completion_day_level']
 m['times']={}
 m['best']=[None,None]
 for c in sorted(com,key=int):
  D=int(c)
  S='\t%2d'%int(c)
  d=[]
  for s in com[c]:
   t=datetime.fromtimestamp(int(com[c][s]['get_star_ts']))
   d+=[t]
   S+='\t%s'%str(d[-1])[5:]
   if s=='1':
    dt = t-days[D-1]
    m['times'][D]=[dt]
    if m['best'][0] is None or dt<m['best'][0]:m['best'][0]=dt
  if len(d)==2:
   dt2=d[1]-d[0]
   S+='\t%s'%(dt2)
   m['times'][D]+=[dt2]
   if m['best'][1] is None or dt2<m['best'][1]:m['best'][1]=dt2
  sys.stdout.write(S+'\n')
 best[m['name']]=m['best']
sys.stdout.write('\n')


b1=[[(best[n][i],n)for n in best if best[n][i]is not None]for i in 0,1]

for i in 0,1:
 sys.stdout.write('Part %d:\n'%(i+1))
 for v,n in sorted(b1[i]):
  sys.stdout.write('\t%s \t%s\n'%(v,n))
 sys.stdout.write('\n')
