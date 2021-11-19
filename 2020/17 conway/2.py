# %%
import numpy as np

with open('input') as f:
    gen = np.array([
        [int(c == '#') for c in list(l)] 
        for l in f.read().split()
    ])

def build_piece(
        arr,
        val,
        slice = 0,
        active_slice = True
    ):
    piece = np.full(
        tuple(s+2 for s in arr.shape[1:]), 
        val
    ).astype(int)
    if active_slice:
        piece[1:-1, 1:-1, 1:-1] = arr[slice]
    return piece

def pad(arr, val):
    paddedCube = np.array([
        build_piece(arr, val, active_slice = False),
        * [build_piece(arr, val, i) for i in range(arr.shape[0])],
        build_piece(arr, val, active_slice = False)
    ])
    return paddedCube

class Cube():
    def __init__(self, gen):
        self.arr = gen
        while self.arr.ndim < 4:
            self.arr = self.arr.reshape(
                1, 
                * self.arr.shape
            )
        self.arr = pad(self.arr, 0)
        self.padded = pad(self.arr, -1)
    def __repr__(self):
        return str(self.arr).replace('0','.').replace('1','#')
    def get_neighbors(self,x,y,z, w):
        i, j, k, l = x+1, y+1, z+1, w+1
        all_around = list(self.padded[i-1:i+2, j-1:j+2, k-1:k+2, l-1:l+2].flatten())
        val = all_around.pop(40)
        return val, sum([n for n in all_around if n != -1])
    def cycle(self):
        nextArr = self.arr.copy()
        for i,_ in enumerate(self.arr):
            for j,_ in enumerate(self.arr[i]):
                for k,_ in enumerate(self.arr[i,j]):
                    for l,_ in enumerate(self.arr[i,j,k]):
                        is_active, neighbors = self.get_neighbors(i,j,k, l)
                        if (is_active and neighbors in [2,3]):
                            nextArr[i,j,k,l] = 1
                        elif (not is_active and neighbors == 3):
                            nextArr[i,j,k,l] = 1
                        else:
                            nextArr[i,j,k,l] = 0
        return Cube(nextArr)

                    

cube = Cube(gen)

for i in range(6):
    cube = cube.cycle()

print(cube.arr.sum())

# %%

# %%
