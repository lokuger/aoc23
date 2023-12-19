import re

def main():
    with open('input19.txt') as f:
        workflows,parts = f.read().split('\n\n')
        workflows = workflows.split()
        parts = parts.split()
    
    print('Part 1: {}'.format(part1(workflows,parts)))
    print('Part 2: {}'.format(part2(workflows)))

def eval_part(name,vals,R):
    if name == 'A': return True
    if name == 'R': return False
    workflow = R[name]
    for c,o,t,target in re.findall('([xmas])(<|>)(\d+):([a-zAR]+)',workflow):
        if (o == '>' and vals['xmas'.index(c)] > int(t)) or (o == '<' and vals['xmas'.index(c)] < int(t)): 
            return eval_part(target,vals,R)
    return eval_part(workflow.split(',')[-1],vals,R)

def part1(workflows,parts):
    # preprocess workflows
    R = {(m:=re.match('^([a-z]+)\{(.*)\}',line)).group(1): m.group(2) for line in workflows}

    # process parts
    s = 0
    for part in parts:
        m = re.match('\{x=(\d+),m=(\d+),a=(\d+),s=(\d+)\}',part)
        s += sum(vals) if eval_part('in',(vals:=[int(m.group(i)) for i in range(1,5)]),R) else 0
    return s
        
# part 2: iterate workflows and split ranges instead of iterating parts
def eval_workflow(v,wf):
    V = []
    for c,o,t,target in re.findall('([xmas])(<|>)(\d+):([a-zAR]+)',wf):
        idx = 'xmas'.index(c)
        t = int(t)
        if o == '<':
            V.append([[v[idx][0], t] if i==idx else [r for r in x] for i,x in enumerate(v[:4])] + [target])
            v[idx][0] = t
        if o == '>':
            V.append([[t+1, v[idx][1]] if i==idx else [r for r in x] for i,x in enumerate(v[:4])] + [target])
            v[idx][1] = t+1
    V.append([*v[:4],wf.split(',')[-1]])
    return V
        

def part2(workflows):
    R = {(m:=re.match('^([a-z]+)\{(.*)\}',line)).group(1): m.group(2) for line in workflows}

    V = [[[1,4001],[1,4001],[1,4001],[1,4001],'in']]
    t = 0
    while V:
        v = V.pop(0)
        if v[4] == 'A':
            t += (v[0][1]-v[0][0])*(v[1][1]-v[1][0])*(v[2][1]-v[2][0])*(v[3][1]-v[3][0])
        elif not v[4] == 'R':
            V.extend(eval_workflow(v,R[v[4]]))
    return t
        
        
if __name__ == '__main__':
    main()