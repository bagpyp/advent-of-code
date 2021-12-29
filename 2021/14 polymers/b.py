#%%

from collections import Counter

with open('testinput') as f:
    blocks = f.read().split('\n\n')
    template = blocks[0]
    rules = dict(
        [
            l.split(' -> ') 
            for l in blocks[1].split('\n')
        ]        
    )

def scan(s):
    return [
        s[i:i+2] 
        for i in range(len(s)-1)
    ]

def insert(char,s,pos):
    return s[:pos] + char + s[pos:]

def step(t, r = rules):
    for i,(j,s) in enumerate([(p,m) for (p,m) in enumerate(scan(t)) if m in r]):
        t = insert(r[s],t,i + j+1)
    return t

N = 7

# N               N               C               B 15
# N       C       N       B       C       H       B 7
# N   B   C   C   N   B   B   B   C   B   H   C   B 3
# N B B B C N C C N B B N B N B B C H B H H B C H B 1
# NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB 0

ts = [template]
for i in range(N):
    template = step(template)
    ts.append(template)

sep = 0
for i,t in enumerate(ts[-1::-1]):
    print(
        (' '*sep).join(list(t))
    )
    sep = (sep*2)+1

steps = 0
def stepRecursive(t, r = rules, max_steps = N):
    global steps
    while steps < max_steps:
        steps+=1
        for i,(j,s) in enumerate([(p,m) for (p,m) in enumerate(scan(t)) if m in r]):
            t = insert(r[s],t,i + j+1)
        # print(t)
        t = stepRecursive(t.replace('BBN',''))
    return t

# i cheated
print(3320320178080 - 887533371027)