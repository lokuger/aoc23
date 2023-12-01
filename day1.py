import re

def main():
    with open('input1.txt') as f:
        input = f.readlines()
    
    #part1(input)
    part2(input)

def part1(input):
    s=0
    for line in input:
        s+=int(re.findall(r'\d', line)[0]+re.findall(r'\d', line)[-1])
    print(s)

d = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
def part2(input):
    s=0
    t = '|'.join(d.keys())
    print(t)
    for i,line in enumerate(input):
        s1 = re.findall(r'(?=(\d|'+t+'))', line)[0]
        s2 = re.findall(r'(?=(\d|'+t+'))', line)[-1]
        try:
            a1 = int(s1)
        except ValueError:
            a1 = d[s1]
        try:
            a2 = int(s2)
        except ValueError:
            a2 = d[s2]
        s+= 10*a1 + a2
    print(s)

if __name__ == '__main__':
    main()