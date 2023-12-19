import re 

def main():
    with open('input18.txt') as f:
        input = f.readlines()
    #input = ['R 2 (#aaaaaa)\n','D 2 (#aaaaaa)\n','R 2 (#aaaaaa)\n','D 2 (#aaaaaa)\n','L 4 (#aaaaaa)\n','U 4 (#aaaaaa)\n']
    print('Part 1: {}'.format(part1(input)))
    print('Part 2: {}'.format(part2(input)))

d = {'R':(0,1),'L':(0,-1),'U':(-1,0),'D':(1,0)}
def part1(input):
    A = [(0,0)]
    s = 0 # for trapezoid formula
    t = 0 # length of circumference - 1 on each segment to add margin
    for k,line in enumerate(input):
        m = re.match('([RDLU]) (\d+) \(#([0-9a-f]{6})\)',line)
        w,n = m.group(1), int(m.group(2))
        s += -(2*A[k][0]+n*d[w][0]+1)*(n*d[w][1]) # trapezoid formula for polygon area
        t += n-1
        A.append((A[k][0]+n*d[w][0],A[k][1]+n*d[w][1]))
    n_cvx = len(input)/2+2  # number of convex corners
    n_ccv = len(input)/2-2  # number of concave corners
    return int(s/2 + t/2 + 3*n_cvx/4 + n_ccv/4)

d2 = {0:'R',1:'D',2:'L',3:'U'}
def part2(input):
    A = [(0,0)]
    s = 0 # for trapezoid formula
    t = 0 # length of circumference - 1 on each segment to add margin
    for k,line in enumerate(input):
        m = re.match('[RDLU] \d+ \(#([0-9a-f]{5})([0-9a-f]{1})\)',line)
        w,n = d2[int(m.group(2))], int(m.group(1),base=16)
        s += -(2*A[k][0]+n*d[w][0]+1)*(n*d[w][1]) # trapezoid formula for polygon area
        t += n-1
        A.append((A[k][0]+n*d[w][0],A[k][1]+n*d[w][1]))
    n_cvx = len(input)/2+2  # number of convex corners
    n_ccv = len(input)/2-2  # number of concave corners
    return int(s/2 + t/2 + 3*n_cvx/4 + n_ccv/4)

if __name__ == '__main__':
    main()