def main():
    with open('input10.txt') as f:
        input = f.readlines()
    
    print('Part 1: {}'.format(part1(input)))
    print('Part 2: {}'.format(part2(input)))

def find_start(input):
    # find start position and initial direction
    for i1,line in enumerate(input):
        if 'S' in line:
            i2 = line.rfind('S')
            if line[i2+1] in 'J-7': dir = 'R'
            elif line[i2-1] in 'L-F': dir = 'L'
            else: dir = 'D'
            break
    return (i1,i2),dir

# dict gives position index and direction updates
d = {'U':((-1,0),{'F':'R','|':'U','7':'L','S':'X'}),
     'D':((1,0),{'L':'R','|':'D','J':'L','S':'X'}),
     'R':((0,1),{'J':'U','-':'R','7':'D','S':'X'}),
     'L':((0,-1),{'L':'U','-':'L','F':'D','S':'X'})}

def part1(input):
    (i1,i2),dir = find_start(input)
    k = 0
    while k < 100000:
        k+=1
        s = d[dir]
        i1,i2 = i1+s[0][0], i2+s[0][1]
        dir = s[1][input[i1][i2]]
        if dir == 'X': return int(k/2)

def part2(input):
    ''' 
    idea: check how many pipes leave a line vertically in both directions.
    Tile is enclosed by loop if and only if numbers of pipes leaving to top and bottom of line
    to the left of current tile are both odd
    '''
    C = [['.']*(len(input[0])-1) for _ in range(len(input))]
    (i1,i2),dir = find_start(input)
    dir_init = dir
    while True:
        s = d[dir]
        i1,i2 = i1+s[0][0], i2+s[0][1]
        C[i1][i2] = input[i1][i2]
        dir = s[1][input[i1][i2]]
        if dir == 'X':break
    
    count_enclosed = 0
    for j1,line in enumerate(C):
        cu,cd = 0,0
        for j2,char in enumerate(line):
            if char in 'FS7': cd +=1   # S as well because it takes role of an F in the input
            if char == '|': cu += 1; cd += 1
            if char in 'LJ': cu += 1
            if C[j1][j2] == '.' and cd%2 == 1 and cu%2 == 1: 
                C[j1][j2] = 'O'; 
                count_enclosed += 1
    # with open('output10.txt','w') as f:
    #     f.write('\n'.join([''.join(r) for r in C]))
    return count_enclosed



if __name__ == '__main__':
    main()