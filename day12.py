from functools import cache 
from re import match 

def main():
    with open('input12ex.txt') as f:
        input = f.readlines()
    
    print('Part 1: {}'.format(part1(input)))
    print('Part 2: {}'.format(part2(input)))

@cache
def f(s,g):
    if len(s)==0:
        return len(g) == 0
    else :
        a = f(s[1:],g) if s[0] != '#' else 0
        b = f(s[g[0]+1:],g[1:]) if (len(g)>0 and match(r'[#?]{%d}[.?]'%g[0],s)) else 0
        return a + b
    
def part1(input):
    n = 0
    for line in input:
        a = line.split()
        v = a[0] + '.'
        w = [int(x) for x in a[1].split(',')]
        n += f(v,tuple(w))
    return n

def part2(input):
    n = 0
    for line in input:
        a = line.split()
        v = '?'.join([a[0]]*5) + '.'
        w = [int(x) for x in a[1].split(',')*5]
        n += f(v,tuple(w))
    return n

if __name__ == '__main__':
    main()