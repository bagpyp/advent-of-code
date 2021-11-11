#%%
import re

with open('input') as f:
    seats = [
        (
            s[:7].replace('F','0').replace('B','1'),
            s[7:].replace('L','0').replace('R','1')
        ) for s in f.read().split('\n')
    ]
    # ..., ('FBBFFBF', 'LLR')]
    
ids = [8*int(s[0],2) + int(s[1],2) for s in seats]

i = max(ids)

for n in range(min(ids),max(ids)+1):
    if n not in ids:
        print(n)
# %%
