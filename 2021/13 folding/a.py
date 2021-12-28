#%%

import numpy as np

with open('input') as f:
    blocks = f.read().split('\n\n')
    dots = [
        (
            int(p[0]),
            int(p[1])
        ) 
        for p in [
            l.split(',') 
            for l in blocks[0].split('\n')
        ]
    ]
    lines = [
        (
            int(l.split('=')[-1]) if 'x' in l else 0, 
            int(l.split('=')[-1]) if 'y' in l else 0
        )
        for l in blocks[1].split('\n')
    ]

paper = np.zeros(
    [
        2 * max([l[a] for l in lines[:2]]) + 1
        for a in (0,1)
    ]
).astype(int)

for d in dots:
    paper[d] = 1

def fold(l, arr):
    m,n = l
    if m:
        for i in range(m):
            arr[i,:] += arr[(2*m)-i,:]
        arr = arr[:m,:]
    elif n:
        for j in range(n):
            arr[:,j] += arr[:,(2*n)-j]
        arr = arr[:,:n]
    return arr.astype(int)

if __name__ == '__main__':
    paper = fold(lines[0],paper)
    print(sum(sum(paper > 0)))
# %%
