#%%
from functools import reduce

with open('input') as f:
    groups = f.read().split('\n\n')

acc = 0

for g in groups:
    surveys = g.split('\n')
    # for a, change intersection to union
    groupAnswers = reduce(set.intersection, [set(s) for s in surveys])
    acc += len(groupAnswers)

print(acc)

# %%
