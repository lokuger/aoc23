def main():
    with open('input13.txt') as f:
        input = f.read()
    
    print('Part 1: {}'.format(part1(input)))
    print('Part 2: {}'.format(part2(input)))

def g(A,d):
    pos = 0
    while pos < len(A[0])-1:
        if sum([sum([abs(c1-c2) for c1,c2 in zip(a[pos::-1],a[pos+1:])]) for a in A]) == d: return pos+1
        pos += 1
    return None

def f(A,d):
    return v if (v:=g(A,d)) is not None else 100*g(list(map(list, zip(*A))),d)

def h(input,d):
    return sum([f([[1 if c =='#' else 0 for c in line] for line in block.split('\n')],d) for block in input.split('\n\n')])

def part1(input):
    return h(input,0)

def part2(input):
    return h(input,1)

if __name__ == '__main__':
    main()