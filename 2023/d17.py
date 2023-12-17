DAY,_,_=__file__.rpartition('.')

from img.img import write_img_fromlist
import heapq

COLS = {
    '.': (255, 255, 255),
    '1': (10, 10, 10),
    '2': (20, 20, 20),
    '3': (30, 30, 30),
    '4': (40, 40, 40),
    '5': (50, 50, 50),
    '6': (60, 60, 60),
    '7': (70, 70, 70),
    '8': (80, 80, 80),
    '9': (90, 90, 90),    
}

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]
        
        
W,H=len(r[0]),len(r)
write_img_fromlist(r,f'{DAY}_0',COLS)

def f(part,MIN,MAX):
    q=[[0,0,0,0,0,[]],[0,0,0,1,0,[]]]
    heapq.heapify(q)
    s=set()
    while 1:
        cost,x,y,d,m,path=heapq.heappop(q)
        if [x,y]==[W-1,H-1]:
            r2=[*map(list,r)]
            for x,y,_ in path:
                r2[y][x]='.'
            write_img_fromlist(r2,f'{DAY}_{part}',COLS)
            return cost
        if (x,y,d,m)in s:continue
        s|={(x,y,d,m)}
        if m<MAX:
            dx,dy=[[1,0],[0,1],[-1,0],[0,-1]][d]
            X,Y=x+dx,y+dy
            if 0<=X<W and 0<=Y<H:
                heapq.heappush(q,[cost+int(r[Y][X]),X,Y,d,m+1,path+[(X,Y,m)]])
        if m>=MIN:
            for dl in (d-1)%4,(d+1)%4:
                dx,dy=[[1,0],[0,1],[-1,0],[0,-1]][dl]
                X,Y=x+dx,y+dy
                if 0<=X<W and 0<=Y<H:
                    heapq.heappush(q,[cost+int(r[Y][X]),X,Y,dl,1,path+[(X,Y,m)]])

print(f(1,1,3))
print(f(2,4,10))


