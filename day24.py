import numpy as np

def main():
    with open('input24.txt') as f:
        input = f.read().strip().split('\n')
    
    print('part 1: {}'.format(part1(input)))
    print('part 2: {}'.format(part2(input)))

# p1 + t1*d1 = p2 + t2*d2
# [d1, -d2] * [t1,t2]^T = p2-p1
# d1[0]*t1 - d2[0]*t2 = p2[0]-p1[0]
# d1[1]*t1 - d2[1]*t2 = p2[1]-p1[1]
def part1(input):
    xmin,xmax,ymin,ymax = 200000000000000,400000000000000,200000000000000,400000000000000
    S = [tuple(tuple(int(r) for r in x.split(',')[:2]) for x in line.split('@')) for line in input]
    n = 0
    for i,sA in enumerate(S):
        for sB in S[i+1:]:
            p1,d1 = sA
            p2,d2 = sB
            if abs(d:=(-d1[0]*d2[1] + d1[1]*d2[0])) < 1e-8: continue # p1rallel
            t1 = 1/d * (-d2[1]*(p2[0]-p1[0]) + d2[0]*(p2[1]-p1[1]))
            t2 = 1/d * (-d1[1]*(p2[0]-p1[0]) + d1[0]*(p2[1]-p1[1]))
            if t1>=0 and t2>=0 and xmin <= (xi:=p1[0]+t1*d1[0]) and xi <= xmax and ymin <= (yi:=p1[1]+t1*d1[1]) and yi <= ymax:
                n += 1
    return n

#  X+ti*Y = Pi+ti*di                            for all i
# -> X-pi = ti*(di - Y)                         for all i
# since we have enough equations look at the implied weaker condition that X-pi and di-Y are parallel so
# (X - pi) x (di - Y) = 0                       for all i
# -> X x di + pi x Y - pi x di = X x Y          for all i
# quadratic term X x Y is common to each eq. i, so can be eliminated. Three stones should be enough to solve:
# pi x di - pj x dj = X x (di-dj) + (pi-pj) x Y        (3 eq.)
# pi x di - pk x dk = X x (di-dk) + (pi-pk) x Y        (3 eq.)
#
def part2(input):
    pi,di = [np.array([int(r) for r in x.split(',')]) for x in input[1].split('@')]
    pj,dj = [np.array([int(r) for r in x.split(',')]) for x in input[24].split('@')]
    pk,dk = [np.array([int(r) for r in x.split(',')]) for x in input[7].split('@')]
    A = np.zeros((6,6))
    for i in range(3):
        x = np.zeros((3,))
        x[i] = 1
        A[:3,i] = np.cross(x,di-dj)
        A[:3,3+i] = np.cross(pi-pj,x)
        A[3:,i] = np.cross(x,di-dk)
        A[3:,3+i] = np.cross(pi-pk,x)
    b = np.concatenate([np.cross(pi,di)-np.cross(pj,dj),np.cross(pi,di)-np.cross(pk,dk)],axis=0)
    X = np.linalg.solve(A,b)
    print(X)
    return np.sum(X[:3])

if __name__ == '__main__':
    main()