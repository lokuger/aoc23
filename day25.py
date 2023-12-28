import re
import numpy as np
from numpy.random import choice

def main():
    with open('input25cut.txt') as f:
        input = f.read().strip().split('\n')
    
    print('Part 1: {}'.format(part1(input)))
    print('Part 2: {}'.format(part2(input)))

def bfs_count_component(G,start):
    Q = [start]
    V = set()
    while Q:
        q = Q.pop(0)
        V.add(q)
        for v in G[q]:
            if v not in V: Q.append(v)
    return len(V)

def construct_graph(input):
    G = {}
    for line in input:
        u,V = line.split(':')[0],line.split(':')[1].strip().split()
        if u not in G: G[u] = []
        for v in V: 
            G[u].append(v)
            if v in G: 
                G[v].append(u)
            else:
                G[v] = [u]
    return G

######## soln using graph viz
# def part1(input):
#     with open('output25.txt','w') as f:
#         f.write('\n'.join([line.split(':')[0] + ' -- ' + ','.join(line.split(':')[1].strip().split()) for line in input]))
#     # now delete 3 edges manually, saved input25cut.txt and run again on that input file
#     G = construct_graph(input)
#     return bfs_count_component(G,'vfx') * bfs_count_component(G,'bgl')

def karger(G):
    N = [u for u in G]
    W = [len(G[u]) for u in G]
    nE = sum(W)
    while len(N) > 2:
        #print('Current graph: {}'.format(G))
        # draw random edge
        iu = choice(len(N),p=np.array(W)/nE)
        u = N[iu]
        tu = G.pop(u)
        v = tu.pop(choice(len(tu)))
        N.pop(iu)
        iv = N.index(v)
        tv = G.pop(v)
        N.pop(iv)
        tv.remove(u)
        #print('Collapse {} -- {}'.format(u,v))
        # collapse edge
        uv = u+v
        tuv = [w for w in tu+tv if w not in [u,v]]
        n_cllps = 2+sum([1 if w in [u,v] else 0 for w in tu+tv])
        #print('Neighbors of collapsed nodes: {}'.format(tuv))
        N.append(uv)
        nu = W.pop(iu)
        nv = W.pop(iv)
        W.append(nu+nv-n_cllps)
        nE -= n_cllps
        G[uv] = tuv
        # replace u and v by uv in neighboring nodes of both
        for w in G[uv]:
            G[w] = [uv if x in [u,v] else x for x in G[w]]
    return int(len(N[0])/3), int(len(N[1])/3)


def part1(input):
    G = construct_graph(input)
    a,b = karger(G)
    print(a,b,a*b)
    #for c in C: G[c[0]].remove(c[1])
    #return bfs_count_component(G,C[0][0]) * bfs_count_component(G,C[0][1])

def part2(input):
    pass

if __name__ == '__main__':
    main()