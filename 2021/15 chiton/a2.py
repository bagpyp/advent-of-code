#%%

import matplotlib.pyplot as plt
import numpy as np

with open('testinput') as f:
    cave = np.array([
        [int(i) for i in r]
        for r in f.read().splitlines()
    ])

plt.imshow(cave, cmap='binary')

N = len(cave) -1
max = int(''.join(np.ones(N*2).astype(int).astype(str)),2)

paths = [bin(i)[2:].zfill(2*N) for i in range(max) 
    if len([s for s in bin(i)[2:] if s == '1']) == N
]

paths_to_ignore = ['2']
def count_path(path, min=41):
    if any([path.startswith(prefix) for prefix in paths_to_ignore]):
        return 
    # display = np.zeros((N+1,N+1))
    p = [0,0]
    # display[tuple(p)] = 1
    acc = 0
    for i,b in enumerate(path):
        if acc >= min:
            paths_to_ignore.append(path[:i])
            break
        if int(b):
            p[1] += 1
        else:
            p[0] += 1
        # display[tuple(p)] = 1
        acc += cave[tuple(p)]
    # plt.imshow(display, cmap='binary')
    # plt.pause(.001)
    return acc

minPath = 999999
path_counts = []

from tqdm import tqdm
for p in tqdm(paths):
    path_count = count_path(p,minPath)
    if path_count:
        path_counts.append(path_count)
        minPath = min(path_count, minPath)

print(min(path_counts))
