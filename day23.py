def main():
    with open('input23.txt') as f:
        input = f.read().strip().split()
    
    print('Part 1: {}'.format(part1(input)))
    print('Part 2: {}'.format(part2(input)))

D1 = {(0,1):'>', (0,-1):'<', (-1,0):'^', (1,0):'v'}
D2 = {'>':(0,1), '<':(0,-1), '^':(-1,0), 'v':(1,0)}
def construct_graph(input,part):
    N = len(input)
    assert(len(input[0])==N)
    fork = [[(0,1),[(1,0)]]]
    G = {(0,1):[]}
    while fork:
        s,c,d = fork[0][0],fork[0][0],fork[0][1].pop(0)
        if len(fork[0][1]) == 0: fork.pop(0)
        l,junction,found_exit = 0,False,False
        while not (junction or found_exit):
            c,d,junction,l = step(input,c,d,l)
            if c == (N-1,N-2): found_exit = True
        if c not in G: 
            G[c] = []
            if junction: fork.append([c,[d for d in D1 if input[c[0]+d[0]][c[1]+d[1]] == D1[d]]])
        G[s].append((c,l))
        if part == 2: G[c].append((s,l))
    return G

def step(input,c,d,l):
    if (s:=input[c[0]][c[1]]) in '<>^v' and l>1:
        return (c[0]+(d:=D2[s])[0],c[1]+d[1]),d,True,l+1
    else:
        for dnew in [d,(d[1],-d[0]),(-d[1],d[0])]:
            if input[(p:=(c[0]+dnew[0],c[1]+dnew[1]))[0]][p[1]] in '.<>^v': return p,dnew,False,l+1

def bellman_ford(G):
    dist = {v:float('inf') for v in G}
    dist[(0,1)] = 0
    
    for _ in range(len(G)-1):
        for u in G:
            for v,c in G[u]:
                if dist[u] + c < dist[v]:
                    dist[v] = dist[u] + c
    return dist

def exhaustive_dfs(s,t,G,curr_cost=0,max_cost=0,M=None):
    if M is None: M = {v:True for v in G}
    if s==t: return max(curr_cost,max_cost)
    if M[s]:
        M[s] = False
        for v,c in G[s]:
            max_cost = exhaustive_dfs(v,t,G,curr_cost+c,max_cost,M)
        M[s] = True
    return max_cost

# graph in part 1 seems to be DAG, so longest path is computable as shortest path on -G by Bellman-Ford
# after implementing part 2 and thinking more, can also just use exhaustive DFS...
def part1(input):
    N = len(input)
    G = construct_graph(input,1)
    #dist = bellman_ford({u:[(v,-c) for v,c in G[u]] for u in G})
    #return -dist[(N-1,N-2)]
    return exhaustive_dfs((0,1),(N-1,N-2),G)

def part2(input):
    N = len(input)
    G = construct_graph(input,2)
    return exhaustive_dfs((0,1),(N-1,N-2),G)

if __name__ == '__main__':
    main()