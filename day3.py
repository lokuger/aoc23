import re

def main():
    with open('input3.txt') as f:
        input = f.readlines()
    
    part1(input)
    part2(input)

def part1(input):
    # find numbers using regex finditer
    q = 0
    for i,line in enumerate(input):
        mtchs = re.finditer('\d+',line)
        for m in mtchs:
            num = int(m.group(0))
            s,e = m.span()
            if s>0:
                if line[s-1] != '.': q += num; continue
                s -= 1
            if e<len(line)-1: # len - 1 because \n at end of line counts towards len
                if line[e] != '.': q += num; continue
                e += 1
            if i>0 and re.search('[^.0-9]',input[i-1][s:e]) is not None: q += num; continue
            if i<len(input)-1 and re.search('[^.0-9]',input[i+1][s:e]) is not None: q += num; continue
    print(q)

def part2(input):
    q = 0
    for i,line in enumerate(input):
        m_gears = re.finditer('\*',line)
        for mg in m_gears:
            s = mg.start()
            n,p = 0,1
            if i>0:
                m_nums = re.finditer('\d+',input[i-1])
                for mn in m_nums:
                    a1,a2 = mn.span()
                    if s >= a1-1 and s <= a2: 
                        n += 1
                        p *= int(mn.group())
            if i<len(input)-1:
                m_nums = re.finditer('\d+',input[i+1])
                for mn in m_nums:
                    a1,a2 = mn.span()
                    if s >= a1-1 and s <= a2: 
                        n += 1
                        p *= int(mn.group())
            if s > 0 and line[s-1] != '.': 
                n += 1
                p *= int(re.match('\d+',line[s-1::-1]).group(0)[::-1])
            if s < len(line)-2 and line[s+1] != '.': 
                n += 1
                p *= int(re.match('\d+',line[s+1:]).group(0))
            if n==2: q += p
    print(q)
         

if __name__ == '__main__':
    main()