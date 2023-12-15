def main():
    with open('input14.txt') as f:
        input = f.readlines()
    
    print('Part 1: {}'.format(part1(input)))
    print('Part 2: {}'.format(part2(input)))

def totalload(A):
    return sum(sum(i+1 for i, c in enumerate(l[::-1]) if c == 'O') for l in A)

def rollnorth(A):
    return tuple("#".join('O'*s.count('O')+'.'*s.count('.') for s in l.split('#')) for l in A)

def rotate(A):
    return tuple(''.join(l) for l in zip(*A))[::-1]

def spin(A):
    for _ in range(4):
        A = rollnorth(A)
        A = rotate(A)
    return A

def f(input):
    return tuple(''.join(s) for s in zip(*input))[:-1] #allows hashing and removes \n column

def part1(input):
    return totalload(rollnorth(f(input)))

def part2(input):
    A = f(input)
    d,i = {},0
    while A not in d and i < 10**9:
        d[A] = i
        A = spin(A)
        i+=1
    
    cycle_length = i-d[A]
    for _ in range((10**9-i)%cycle_length):
        A = spin(A)
    return totalload(A)

if __name__ == '__main__':
    main()