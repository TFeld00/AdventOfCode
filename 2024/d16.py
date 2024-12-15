DAY,_,_=__file__.rpartition('.')

import heapq
from alg.dijkstra import get_dijkstra_path
from img.img import write_img_fromlist

COLS = {
    '.': (255, 255, 255),
    '#': (0, 0, 0),
    'S': (255, 0, 0),
    'E': (0, 255, 0),
    'O': (120, 120, 120),
}

from alg.file import download_input
download_input(DAY)

r=[]
i=0
with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        
        if 'S' in l:
            X,Y=l.find('S'),i
        if 'E' in l:
            tX,tY=l.find('E'),i
        i+=1

        l=list(l)
        r+=[l]

def dijkstra(graph, starting_vertex):
    distances = {vertex: (float('infinity'), None) for vertex in graph}
    distances[starting_vertex] = (0, None)
    prevs={vertex: set() for vertex in graph}

    pq = [(0, starting_vertex, None)]
    while len(pq) > 0:
        current_distance, current_vertex, path = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex][0]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better than any path we've
            # already found.
            if distance <= distances[neighbor][0]:
                 prevs[neighbor] = prevs.get(neighbor,{})|{current_vertex}
            if distance < distances[neighbor][0]:
                distances[neighbor] = (distance, current_vertex)
                heapq.heappush(pq, (distance, neighbor, current_vertex))

    return distances,prevs

# Build graph
g={}
for i,l in enumerate(r):
    for j,c in enumerate(l):
        if c in 'S.E':
            for d in 0,1,2,3:
                g[(j,i,d)]=g.get((j,i,d),{})
                for dd in -1,1:
                    g[(j,i,d)][(j,i,(d+dd)%4)]=1000
                dx,dy=[(1,0),(0,1),(-1,0),(0,-1)][d]
                x,y=j+dx,i+dy
                if r[y][x] in 'S.E':
                    g[(j,i,d)][(x,y,d)]=1

# Dijkstra
res,prevs=dijkstra(g,(X,Y,0))
S,V=min([res[(tX,tY,d)]for d in (0,1,2,3)])

# Part 1
print(S)

# Part 2
t={(tX,tY),V[0:2]}
q=[V]
for v in q:
    w=prevs[v]
    q+=[*w]
    t|={(x,y)for x,y,_ in w}

print(len(t))

# Print
write_img_fromlist(r,f'{DAY}_0',COLS)
for x,y,_ in get_dijkstra_path(res,V):
    if r[y][x]=='.':
        r[y][x]='O'
write_img_fromlist(r,f'{DAY}_1',COLS)
for x,y in t:
    if r[y][x]=='.':
        r[y][x]='O'

write_img_fromlist(r,f'{DAY}_2',COLS)