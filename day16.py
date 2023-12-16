def main():
    with open('input16.txt') as f:
        input = f.readlines()
    
    print('Part 1: {}'.format(part1(input)))
    print('Part 2: {}'.format(part2(input)))

D = {'.':{'R':'R', 'L':'L', 'U':'U', 'D':'D'},
     '-':{'R':'R', 'L':'L', 'U':['L','R'], 'D':['L','R']},
     '|':{'U':'U', 'D':'D', 'L':['U','D'], 'R':['U','D']},
     '/':{'U':'R', 'R':'U', 'L':'D', 'D':'L'},
     '\\':{'U':'L', 'L':'U', 'R':'D', 'D':'R'},
     'X':{'D':[], 'U':[], 'R':[], 'L':[]}
     }
I = {'R':(0,1), 'L':(0,-1), 'U':(-1,0), 'D':(1,0)}

def energized(input,istart,jstart,dirstart):
    L = [[input[i][j] if (i>-1 and i<len(input) and j>-1 and j<len(input[0])-1) else 'X' for j in range(-1,len(input[0]))] for i in range(-1,len(input)+1)]
    A = [[0 for _ in range(-1,len(input[0]))] for _ in range(-1,len(input)+1)]
    B = [(istart,jstart,dirstart)]
    A[istart][jstart] = 1
    seen = [(istart,jstart,dirstart)]
    k=0
    while len(B)>0:
        C = []
        for b in B:
            p,q = b[0],b[1]
            dirnew = D[L[p][q]][b[2]]
            for d in dirnew:
                pnew,qnew = p+I[d][0],q+I[d][1]
                A[pnew][qnew] = 1
                if (pnew,qnew,d) not in seen:
                    seen.append((pnew,qnew,d))
                    C.append((pnew,qnew,d))
        k += 1
        B = C
    A = [a[1:-1] for a in A[1:-1]]
    return sum([sum(a) for a in A])

def part1(input):
    return energized(input,1,1,'R')

def part2(input):
    a = 0
    for jstart in range(1,len(input[0])):
        a = max(a,energized(input,1,jstart,'D'),energized(input,len(input),jstart,'U'))
    for istart in range(1,len(input)+1):
        a = max(a,energized(input,istart,1,'R'),energized(input,istart,len(input[0])-1,'L'))
    return a

if __name__ == '__main__':
    main()