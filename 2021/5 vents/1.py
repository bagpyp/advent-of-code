#%%

from parse import compile
import numpy as np
import pandas as pd

p = compile('{a:d},{b:d} -> {c:d},{d:d}')
with open ('testinput') as f:
    lines = [p.parse(l).named for l in f.read().splitlines()]

df = pd.DataFrame(lines)
x = max(df.a.max(),df.c.max())
y = max(df.b.max(),df.d.max())

field = np.zeros((x+1,y+1))


for l in lines:
    x1 = min(l['a'],l['c'])
    x2 = max(l['a'],l['c'])+1
    y1 = min(l['b'],l['d'])
    y2 = max(l['b'],l['d'])+1
    if l['a'] == l['c'] or l['b'] == l['d']:
        field[y1:y2, x1:x2] += 1
    else:
        print(f'{x1},{y1} -> {x2},{y2}')
        for x, y in zip(range(x1,x2+1),range(y1,y2+1)):
            field[x,y] += 1
        print(str(field.astype(int)).replace('0','.'), '\n')



# %%