#%%
from collections import Counter

with open ('testinput') as f:
    input = [int(l) for l in f.read().split(',')]

days = [0] * 9

for i in input:
    days[i] += 1

def cycle(window):
    born_today = window.pop(0)
    window.insert(8,born_today)
    window[6] += born_today
    return window

print(days)
for i in range(256):
    days = cycle(days)
    
print(sum(days))
# %%
