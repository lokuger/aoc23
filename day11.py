def main():
    with open('input11.txt') as f:
        input = f.readlines()
    
    print('Part 1: {}'.format(part1(input)))
    print('Part 2: {}'.format(part2(input)))

def determine_dists(input,factor):
    S = []
    for i,line in enumerate(input):
        for j,c in enumerate(line):
            if c == '#':
                S.append((i,j))
    rows_with_g = set([s[0] for s in S])
    cols_with_g = set([s[1] for s in S])
    rows_inflate = sorted(list(set(range(len(input))).difference(rows_with_g)))
    cols_inflate = sorted(list(set(range(len(input[0])-1)).difference(cols_with_g)))
    d = 0
    for k,s1 in enumerate(S):
        for s2 in S[k+1:]:
            g = lambda l,s,q : next((idx for idx,val in enumerate(l) if val>s[q]),len(l))
            ir = abs(g(rows_inflate,s1,0)-g(rows_inflate,s2,0)) # number of inflated rows between s1 and s2
            ic = abs(g(cols_inflate,s1,1)-g(cols_inflate,s2,1)) # number of inflated cols between s1 and s2
            d += abs(s1[0]-s2[0])+abs(s1[1]-s2[1])+(ir+ic)*(factor-1)
    return(d)

def part1(input):
    return determine_dists(input,2)

def part2(input):
    return determine_dists(input,1000000)

if __name__ == '__main__':
    main()