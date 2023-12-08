import math

def main():
    with open('input6.txt') as f:
        input = f.readlines()
    
    print(part1(input))
    print(part2(input))

def part1(input):
    print('#### Part 1 ####')
    # just for fun, do it as a one-liner
    return math.prod([math.ceil(t/2 + ((t/2)**2-d)**0.5) - math.floor(t/2 - ((t/2)**2-d)**0.5) - 1 for t,d in zip([int(s) for s in input[0].split(':')[1].split()],[int(s) for s in input[1].split(':')[1].split()])])

def part2(input):
    print('#### Part 2 ####')
    t = int(input[0].split(':')[1].replace(' ',''))
    d = int(input[1].split(':')[1].replace(' ',''))
    return math.ceil(t/2 + ((t/2)**2-d)**0.5) - math.floor(t/2 - ((t/2)**2-d)**0.5) - 1

if __name__ == '__main__':
    main()