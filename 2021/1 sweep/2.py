#%%

import numpy as np

with open('input') as f:
    input = [int(l) for l in f.read().splitlines()]

blur = [sum(input[i:i+3]) for i in range(len(input) - 2)]

diff = sum(np.diff(np.array(blur)) > 0)
print(diff)

# %%
