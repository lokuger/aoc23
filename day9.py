import numpy as np
from scipy import special

def main():
    with open('input9.txt') as f:
        input = f.readlines()
    
    print('Part 1: {}'.format(part1(input)))
    print('Part 2: {}'.format(part2(input)))

def part1(input):
    S = 0
    for line in input:
        numbers = [int(s) for s in line.split()]
        L,k = numbers, 0
        allzero = all([n==0 for n in numbers])
        while not allzero:
            k+=1
            L = [a-b for a,b in zip(L[1:],L[:-1])]
            allzero = all([n==0 for n in L])
        binoms = [((-1)**(j+1+k))*special.binom(k,j) for j in range(k)]
        S += sum([a*b for a,b in zip(numbers[-k:],binoms)])
    return S

def part2(input):
    S = 0
    for line in input:
        numbers = [int(s) for s in line.split()]
        L,k = numbers, 0
        allzero = all([n==0 for n in numbers])
        while not allzero:
            k+=1
            L = [a-b for a,b in zip(L[1:],L[:-1])]
            allzero = all([n==0 for n in L])
        binoms = [((-1)**(j+1))*special.binom(k,j) for j in range(1,k+1)]
        S += sum([a*b for a,b in zip(numbers[:k],binoms)])
    return S

if __name__ == '__main__':
    main()