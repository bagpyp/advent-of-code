#%%
import numpy as np

with open('input') as f:
    report = np.array([
        [int(ll) for ll in list(l)] 
        for l in f.read().splitlines()
    ])

gamma = [int(sum(arr)>arr.size/2) for arr in report.T]
epsilon = [int(not g) for g in gamma]

g = int(''.join([str(r) for r in gamma]),2)
e = int(''.join([str(r) for r in epsilon]),2)

print(e*g)
# %%
