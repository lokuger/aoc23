import numpy as np
import heapq

def main():
    with open('input22.txt') as f:
        input = f.readlines()
    
    print('Part 1: {}'.format(part1(input)))
    print('Part 2: {}'.format(part2(input)))

def construct_dependency_graphs(input):
    Q = []
    for i,line in enumerate(input):
        a = [[int(x) for x in h.split(',')] for h in line.split('~')]
        heapq.heappush(Q,(min(a[0][2],a[1][2]),i+1,a))
        
    #A = np.zeros((3,3,10))
    A = np.zeros((10,10,500))
    A[:,:,0] = -1
    k = 1
    G1 = {-1:set()}    # graph with k->l = k supports l
    G2 = {}         # graph with k->l = k is supported by l
    while Q:
        zmin,id,a = heapq.heappop(Q)
        x,dx,y,dy,dz = a[0][0],a[1][0]+1-a[0][0],a[0][1],a[1][1]+1-a[0][1],a[1][2]+1-a[0][2]
        r = np.nonzero(np.sum(A[x:x+dx,y:y+dy,:zmin],axis=(0,1)))[0][-1]+1  # z-index where piece lands
        A[x:x+dx,y:y+dy,r:r+dz] = id
        S = set(int(w) for w in A[x:x+dx,y:y+dy,r-1].flatten()).difference(set([0]))
        G1[id] = set()
        for s in S: G1[s].add(id)
        G2[id] = S
        k+=1
    return G1,G2

def part1(input):
    _,G2 = construct_dependency_graphs(input)
    T = set(range(1,len(input)+1))
    for g in G2:
        if len(s:=G2[g])==1 and (x:=next(iter(s))) in T: T.remove(x)
    return len(T)

def part2(input):
    G1,G2 = construct_dependency_graphs(input)
    T = set(range(1,len(input)+1))
    n = 0
    for t in T:
        P = set([t])  # set of bricks that fall
        Q = G1[t]   # set of bricks for which (some) support is removed when bricks below fall
        while True:
            np,nq = len(P),len(Q)
            for q in Q:
                if not G2[q].difference(P):
                    P.add(q)
                    Q = Q.union(Q,G1[q])
            if np==len(P) and nq==len(Q): break
        n += len(P)-1
    return n            
        


if __name__ == '__main__':
    main()