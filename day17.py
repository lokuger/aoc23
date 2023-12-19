import heapq

def main():
    with open('input17.txt') as f:
        input = f.read().strip().split('\n')
    
    print('Part 1: {}'.format(part1(input)))
    print('Part 2: {}'.format(part2(input)))

def get_neighbors(node,A,minstreak,maxstreak):
    """routine to determine neighbors depending on previous number of steps in direction d"""
    c,q,d,s = node
    opt = []
    if s < maxstreak:
        p = (q[0]+d[0],q[1]+d[1])
        if 0<=p[0] and p[0]<len(A) and 0<=p[1] and p[1]<len(A[0]): opt.append((c+A[p[0]][p[1]],p,d,s+1))
    if s >= minstreak and s <= maxstreak:
        p1,p2 = (q[0]+d[1],q[1]-d[0]),(q[0]-d[1],q[1]+d[0]) # 90 degree turns
        if 0<=p1[0] and p1[0]<len(A) and 0<=p1[1] and p1[1]<len(A[0]):
            opt.append((c+A[p1[0]][p1[1]],p1,(d[1],-d[0]),1))
        if 0<=p2[0] and p2[0]<len(A) and 0<=p2[1] and p2[1]<len(A[0]):
            opt.append((c+A[p2[0]][p2[1]],p2,(-d[1],d[0]),1))
    return opt

def mod_dijkstra(input,mins,maxs):
    A = [[int(c) for c in line] for line in input]
    Q = [] # priority queue with (cost, current pos, current dir, number of steps in that dir)
    heapq.heappush(Q,(0,(0,0),(0,1),0)) # starting east
    heapq.heappush(Q,(0,(0,0),(1,0),0)) # starting south
    V = set()   # visited
    while Q:
        curr = heapq.heappop(Q)
        c,pos,dir,nsteps = curr
        if (pos,dir,nsteps) in V: continue
        else: V.add((pos,dir,nsteps))
        neighbors = get_neighbors(curr,A,mins,maxs)
        for n in neighbors:
            c,posnew,_,_ = n
            if posnew[0]==len(A)-1 and posnew[1]==len(A[0])-1: return c
            heapq.heappush(Q,n)

def part1(input):
    return mod_dijkstra(input,1,3)

def part2(input):
    return mod_dijkstra(input,4,10)

if __name__ == '__main__':
    main()