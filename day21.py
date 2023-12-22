import math

def main():
    with open('input21.txt') as f:
        input = f.read().strip().split('\n')
    
    input_mod = [['.' if x=='S' else x for x in line] for line in input]
    print('Part 1: {}'.format(part1(input_mod)))
    print('Part 2: {}'.format(part2(input_mod)))


def bfs(input,max_dist,start=None,start_dist=0):
    if start is None: start = (int(len(input)/2),int(len(input)/2))
    Q = [(start_dist,start[0],start[1])]
    dist = [[start_dist if (i==start[0] and j==start[1]) else float('inf') for j in range(len(input[0]))] for i in range(len(input))]
    
    while Q:
        q = Q.pop(0)
        if q[0]>max_dist: return dist
        for i,j in [(q[1]+1,q[2]),(q[1]-1,q[2]),(q[1],q[2]+1),(q[1],q[2]-1)]:
            if 0<=i and i<len(input) and 0<=j and j<len(input[0]) and input[i][j]=='.' and dist[i][j] == float('inf'):
                Q.append((q[0]+1,i,j))
                dist[i][j] = q[0]+1
    return dist

def reachable_pots_in_single_map(input,max_dist,start=None,start_dist=0,verbose=False):
    dist = bfs(input,max_dist,start=start,start_dist=start_dist)
    if verbose:
        print('\n'.join(['\t'.join(str(c) for c in line) for line in dist]))
        print('______________________________________')
    return sum([sum([1 if x<=max_dist and x%2==max_dist%2 else 0 for x in line]) for line in dist])

def part1(input):
    return reachable_pots_in_single_map(input,64)

def part2(input):
    """ assumptions that are true in my input: 
    Map is square of side length 2k+1, k odd, Start is in the middle and center axes and boundary are free of rocks
    This makes the boundary perfectly symmetrical, so we can compute how many periodic maps are filled entirely
    and then handle boundaries by running the modified bfs above once for every corner and edge center on the map

    To make things even simpler here N = k mod 2k+1 so that boundaries simplify even a little further
    """
    verbose = False
    N = 26501365
    k = int((len(input)-1)/2)
    print('k: {}'.format(k))

    # determine number of total reachable pots in completely filled maps, odd/even cases
    dist = bfs(input,max_dist=2*k)
    s = sum([sum([1 if x<float('inf') else 0 for x in line]) for line in dist])
    s_odd = sum([sum([1 if x%2==1 else 0 for x in line]) for line in dist])
    s_even = s-s_odd

    # R = # l1 rings of completely explored maps in middle of l1 diamond
    # (assume R is even as in the example)
    # rings 1,3,5,... pots with odd parity have to be counted (s_odd), rings 2,4,6,.. even parity pots are reached (s_even)
    R = math.floor((N+1)/(2*k+1))
    S_odd = (R-1)**2 * s_odd
    S_even = R**2 * s_even

    # since N = k mod 2k+1, there are 3 types of boundary cases
    # type 1 maps are filled from one corner and have N-(N-k+1) = k-1 steps left, will be filled ~1/8 in this corner
    # type 2 maps are filled from one corner and have N-(N-3k) = 3k steps left, will be filled approximately 7/8 up to opposite corner
    # type 3 maps are on the axes (cusps of the l1-diamond) are filled from edge centers with N-(N-2k) = 2k steps left, will be filled ~3/4 up to opposite corners
    T1 = sum(map(lambda x: reachable_pots_in_single_map(input,N,x,N-k+1,verbose=verbose),[(0,0),(2*k,0),(0,2*k),(2*k,2*k)]))
    T2 = sum(map(lambda x: reachable_pots_in_single_map(input,N,x,N-3*k,verbose=verbose),[(0,0),(2*k,0),(0,2*k),(2*k,2*k)]))
    T3 = sum(map(lambda x: reachable_pots_in_single_map(input,N,x,N-2*k,verbose=verbose),[(k,0),(k,2*k),(0,k),(2*k,k)]))
    
    # ring of type 2 maps has (R+1)
    B = T3 + (R-1)*T2 + R*T1
    
    if verbose:
        print('s_odd: {}'.format(s_odd))
        print('s_even: {}'.format(s_even))
        print('R: {}'.format(R))
        print('S_odd: {}'.format(S_odd))
        print('S_even: {}'.format(S_even))
        print('T1: {}'.format(T1))
        print('T2: {}'.format(T2))
        print('T3: {}'.format(T3))
    return B + S_odd + S_even

if __name__ == '__main__':
    main()