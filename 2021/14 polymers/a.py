#%%

from collections import Counter

with open('input') as f:
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

def step(t, r):
    for i,(j,s) in enumerate([(p,m) for (p,m) in enumerate(scan(t)) if m in r]):
        t = insert(r[s],t,i + j+1)
    return t

N = 10

data = [Counter(template)]
for i in range(N):
    template = step(template, rules)
    data.append(Counter(template))

print(max(data[-1].values()) - min(data[-1].values()))


