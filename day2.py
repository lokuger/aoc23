import re

def main():
    with open('input2.txt') as f:
        input = f.readlines()
    
    part1(input)
    part2(input)

def part1(input):
    sumids = 0
    for line in input:
        s = line.split(':')
        id = int(re.findall(r'Game (\d+)',s[0])[0])
        t = s[1].split(';')
        possible = True
        for draw in t:
            b = draw.split(',')
            for p in b:
                r = re.match(r'(\d+) ((?:blue)|(?:green)|(?:red))',p.strip())
                num, col = int(r.group(1)), r.group(2)
                if col == 'red' and num > 12: possible = False
                if col == 'green' and num > 13: possible = False
                if col == 'blue' and num > 14: possible = False
        if possible: 
            sumids += id
    print(sumids)
        
        

def part2(input):
    powers = 0
    for line in input:
        s = line.split(':')
        id = int(re.findall(r'Game (\d+)',s[0])[0])
        t = s[1].split(';')
        minred = 0
        mingreen = 0
        minblue = 0
        for draw in t:
            b = draw.split(',')
            for p in b:
                r = re.match(r'(\d+) ((?:blue)|(?:green)|(?:red))',p.strip())
                num, col = int(r.group(1)), r.group(2)
                if col == 'red' and num > minred: minred = num
                if col == 'green' and num > mingreen: mingreen = num
                if col == 'blue' and num > minblue: minblue = num
        powers += minblue*minred*mingreen
    print(powers)

if __name__ == '__main__':
    main()