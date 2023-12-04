def main():
    with open('input4.txt') as f:
        input = f.readlines()
    
    print('###### Part 1 ######')
    part1(input)
    print('###### Part 2 ######')
    part2(input)

def part1(input):
    s = 0
    for line in input:
        a, b = line.split(':')[1].split('|')
        na, nb = set([int(a[3*i+1:3*i+3]) for i in range(int((len(a)-1)/3))]), set([int(b[3*i+1:3*i+3]) for i in range(int((len(b)-1)/3))])
        p = len(na.intersection(nb))
        if p > 0: s += 2**(p-1)
    print(s)
        

def part2(input):
    n_cards = [1]*len(input)
    print(n_cards)
    for i,line in enumerate(input):
        a, b = line.split(':')[1].split('|')
        na, nb = set([int(a[3*i+1:3*i+3]) for i in range(int((len(a)-1)/3))]), set([int(b[3*i+1:3*i+3]) for i in range(int((len(b)-1)/3))])
        p = len(na.intersection(nb))
        if p > 0: n_cards[i+1:i+p+1] = [m+n_cards[i] for m in n_cards[i+1:i+p+1]]
    print(sum(n_cards))

if __name__ == '__main__':
    main()