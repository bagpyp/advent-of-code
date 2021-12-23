#%%

import numpy as np

with open('input') as f:
    floor = np.array([
        [int(i) for i in list(j)] 
        for j in f.read().split()
    ])

def pad(arr):
    piece = np.full(tuple(s+2 for s in arr.shape), 10).astype(int)
    piece[1:-1, 1:-1] = arr
    return piece

floorPad = pad(floor)

lowPoints = []
for i in range(floor.shape[0]):
    for j in range(floor.shape[1]):
        I = i+1
        J = j+1
        if all([floorPad[neighbor] > floor[(i,j)] for neighbor in [
            (I-1,J),
            (I,J-1),
            (I+1,J),
            (I,J+1)
        ]]):
            lowPoints.append((i,j))

print(lowPoints)

        



def check_neighbors(p: tuple[int]) -> list[tuple[int]]:
    basin.append(p)
    i,j = p
    I = i+1
    J = j+1
    neighbors = [
            (I-1,J),
            (I,J-1),
            (I+1,J),
            (I,J+1)
        ]
    for neighbor in neighbors:
        if floorPad[neighbor] < 9:
            P = (neighbor[0]-1,neighbor[1]-1)
            if P not in basin:
                check_neighbors(P)


def check_basin(basin):
    print(floor)
    arr = np.zeros(floor.shape)
    for p in basin:
        arr[p] = 1



basins = []
for lp in lowPoints:
    basin = []
    check_neighbors(lp)
    basins.append(basin)

print(np.prod(sorted([len(b) for b in basins])[-3:]))



    
# %%
