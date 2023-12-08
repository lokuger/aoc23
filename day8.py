import re, math

def main():
    with open('input8.txt') as f:
        input = f.readlines()
    
    part1(input)
    part2(input)

def part1(input):
    print('#### Part 1 ####')
    steps = input[0]
    C = [re.match('([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)',line) for line in input[2:]]
    K = {C[i].group(1) : i for i in range(len(input[2:]))}
    i = K['AAA']
    k = 0
    while k < 1000000:
        s = C[i].group(2) if steps[k%(len(steps)-1)] == 'L' else C[i].group(3)
        if s == 'ZZZ': print(k+1); break
        else: i = K[s]; k+=1

def part2(input):
    print('#### Part 2 ####')
    steps = input[0]
    C = [re.match('([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)',line) for line in input[2:]]
    K = {C[i].group(1) : i for i in range(len(input[2:]))}
    I = [K[c.group(1)] for c in C if c.group(1)[2]=='A']
    g = 1
    for i in I:
        k = 0
        while True:
            s = C[i].group(2) if steps[k%(len(steps)-1)] == 'L' else C[i].group(3)
            if s[2] == 'Z': g = math.lcm(g,k+1); break
            else: i = K[s]; k+=1
    print(g)
        
        

if __name__ == '__main__':
    main()