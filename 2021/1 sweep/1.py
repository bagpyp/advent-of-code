#%%
import numpy as np

with open('input') as f:
    input = [int(l) for l in f.read().splitlines()]

diff = sum(np.diff(np.array(input)) > 0)
print(diff)
# %%
