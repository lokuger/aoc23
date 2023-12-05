def main():
    with open('input5.txt') as f:
        input = f.readlines()
    
    part1(input)
    part2(input)

def part1(input):
    print('#### Part 1 ####')
    s = [int(x) for x in input[0].split(':')[1].split()]
    i = 3
    while i < len(input)-1: # loop for every block
        t = [(x,0) for x in s]
        while i<=len(input)-1 and input[i][0].isdigit(): # loop for lines within block
            n1,n2,n3 = [int(x) for x in input[i].split()]
            t = [(n1+num-n2,1) if (num>=n2 and num<n2+n3 and t[i][1]==0) else t[i] for i,num in enumerate(s)] # assume that there is no ambiguity/overlap in the map definitions
            i+=1
        i+=2    # jump over the empty and text lines
        s = [x[0] for x in t]
    print(min(s))

def part2(input):
    print('#### Part 2 ####')
    l1 = [int(x) for x in input[0].split(':')[1].split()]
    s = [(a,b) for a,b in zip(l1[::2],l1[1::2])]
    i = 3
    while i < len(input)-1: # loop for every block
        t = [(x,0) for x in s]
        while i<=len(input)-1 and input[i][0].isdigit(): # loop for lines within block
            n1,n2,n3 = [int(x) for x in input[i].split()]
            for j,x in enumerate(s):
                if t[j][1]==0:
                    if x[0]>=n2 and x[0]+x[1]<n2+n3:
                        t[j] = ((n1+x[0]-n2,x[1]),1)
                    elif x[0]>=n2 and x[0]<n2+n3: # range overlaps from right, split up
                        t[j] = ((n1+x[0]-n2,n2+n3-x[0]),1)
                        t.append(((n2+n3,x[0]+x[1]-(n2+n3)),0))
                    elif x[0]<n2 and x[0]+x[1]>=n2 and x[0]+x[1]<n2+n3: # range overlaps from left, split up
                        t[j] = ((x[0],n2-x[0]),0)
                        t.append(((n1,x[0]+x[1]-n2),1))
            i+=1
        i+=2
        s = [x[0] for x in t]
    r = [a for a,_ in s]
    print(min(r))

if __name__ == '__main__':
    main()