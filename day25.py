import re

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

def part1(input):
    #with open('output25.txt','w') as f:
    #    f.write('\n'.join([line.split(':')[0] + ' -- ' + ','.join(line.split(':')[1].strip().split()) for line in input]))

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
    
    return bfs_count_component(G,'vfx') * bfs_count_component(G,'bgl')
            


def part2(input):
    pass

if __name__ == '__main__':
    main()