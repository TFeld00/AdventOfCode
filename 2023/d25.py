DAY,_,_=__file__.rpartition('.')

from math import prod
import networkx as nx

from alg.file import download_input
download_input(DAY)

G=nx.Graph()

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.replace(':','')
        a,*l=l.split()
        for b in l:
            G.add_edge(a,b)

cut=nx.minimum_edge_cut(G)
G.remove_edges_from(cut)

print(prod(len(v)for v in nx.connected_components(G)))
