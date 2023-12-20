import re
import math

def main():
    with open('input20.txt') as f:
        input = f.read().strip().split('\n')
    
    print('Part 1: {}'.format(part1(input)))
    print('Part 2: {}'.format(part2(input)))

def part1(input):
    # ugly dict of form
    #   name : (type, extras, list of destination names). extras is switch for flop flops and inputs for conjunctions
    D = {}
    for line in input:
        m = re.match('^([%|&]?)([a-z]+) -> (.*)',line)
        dests = [d.strip() for d in m.group(3).split(',')]
        if m.group(1) == '%' :
            type = 'F'
            switch = 0
            D[m.group(2)] = [type,switch,dests]
        elif m.group(1) == '&' :
            type = 'C'
            inputs = {re.search('([a-z]+) -> ',l).group(1):'lo' for l in input if (m.group(2) in l.split('>')[1])}
            D[m.group(2)] = [type,inputs,dests]
        else:
            D[m.group(2)] = ['B',dests]

    # process beams
    nlo,nhi = 0,0
    Q = []
    for _ in range(1000):
        Q.append(('button','lo','broadcaster'))
        while Q:
            beam = Q.pop(0)
            #print('{} -{}-> {}'.format(beam[0],'high' if beam[1]=='hi' else 'low',beam[2]))
            if beam[1] == 'lo': 
                nlo += 1
            else:
                nhi += 1
            if beam[2] in D:
                L = D[beam[2]]
                if L[0] == 'B':
                    Q.extend([(beam[2],'lo',d) for d in L[1]])
                if L[0] == 'F' and beam[1] == 'lo':
                    L[1] = 1-L[1]
                    Q.extend([(beam[2],'hi' if L[1] else 'lo',d) for d in L[2]])
                if L[0] == 'C':
                    L[1][beam[0]] = beam[1] # update memory for that input
                    #print('{} has memory state {}'.format(beam[2],L[1]))
                    t = 'lo' if all([t=='hi' for t in L[1].values()]) else 'hi'
                    Q.extend([(beam[2],t,d) for d in L[2]])
    return nlo*nhi

def part2(input):
    # ugly dict of form
    #   name : (type, extras, list of destination names). extras is switch for flop flops and inputs for conjunctions
    D = {}
    for line in input:
        m = re.match('^([%|&]?)([a-z]+) -> (.*)',line)
        dests = [d.strip() for d in m.group(3).split(',')]
        if m.group(1) == '%' :
            type = 'F'
            switch = 0
            D[m.group(2)] = [type,switch,dests]
        elif m.group(1) == '&' :
            type = 'C'
            inputs = {re.search('([a-z]+) -> ',l).group(1):'lo' for l in input if (m.group(2) in l.split('>')[1])}
            D[m.group(2)] = [type,inputs,dests]
        else:
            D[m.group(2)] = ['B',dests]

    # rx receives from conjunction rg. rg sends low if and only if all of its inputs (all conjunctions) send low
    # so lcm of these four input conjunctions' cycles
    C = {input:None for input in D['rg'][1]}
    Q = []
    n_press = 0
    k = 0
    while any([c is None for c in C.values()]):
        n_press += 1
        Q.append(('button','lo','broadcaster'))
        while Q:
            k+=1
            beam = Q.pop(0)
            #print('{} -{}-> {}'.format(beam[0],'high' if beam[1]=='hi' else 'low',beam[2]))
            if beam[2] in D:
                L = D[beam[2]]
                if L[0] == 'B':
                    Q.extend([(beam[2],'lo',d) for d in L[1]])
                if L[0] == 'F' and beam[1] == 'lo':
                    L[1] = 1-L[1]
                    Q.extend([(beam[2],'hi' if L[1] else 'lo',d) for d in L[2]])
                if L[0] == 'C':
                    L[1][beam[0]] = beam[1] # update memory for that input
                    #print('{} has memory state {}'.format(beam[2],L[1]))
                    t = 'lo' if all([t=='hi' for t in L[1].values()]) else 'hi'
                    Q.extend([(beam[2],t,d) for d in L[2]])
            if beam[2] == 'rg' and beam[1] == 'hi' and C[beam[0]] is None:
                C[beam[0]] = (n_press, k)
    return math.lcm(*[c[0] for c in C.values()])

if __name__ == '__main__':
    main()