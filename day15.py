def main():
    with open('input15.txt') as f:
        input = f.read()
    
    print('Part 1: {}'.format(part1(input)))
    print('Part 2: {}'.format(part2(input)))

def h(x):
    n = 0
    for c in x:
        n=((n+ord(c))*17)%256
    return n

def part1(input):
    return sum([h(x) for x in input.split(',')])

def part2(input):
    A = [[] for _ in range(256)]
    for x in input.split(','):
        if '=' in x:
            lab,foc = x.split('=')[0],int(x.split('=')[1])
            p = h(lab)
            idx = next((i for i,x in enumerate(A[p]) if x[0]==lab), None)
            if idx == None: 
                A[p].append((lab, foc))
            else:
                A[p][idx] = (lab, foc)
        else:
            lab = x[:-1]
            p = h(lab)
            idx = next((i for i,x in enumerate(A[p]) if x[0]==lab), None)
            if idx is not None: A[p].pop(idx)
    return(sum([sum([(i+1)*(j+1)*t[1] for j,t in enumerate(a)]) for i,a in enumerate(A)]))

if __name__ == '__main__':
    main()