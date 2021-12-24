#%%
import numpy as np

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

with open('testinput') as f:
    octopi = np.array([
        [int(i) for i in list(j)] 
        for j in f.read().split()
    ])

def pad(arr):
    arrPad = np.full(tuple(s+2 for s in arr.shape), -1).astype(int)
    arrPad[1:-1, 1:-1] = arr
    return arrPad

octopad = pad(octopi)



class Octopus:
    def __new__(cls, i, j):
        if octopad[(i+1, j+1)] > 0:
            return super().__new__(cls)
    
    def __init__(self, i: int, j:int) -> None:
        self.i, self.j = i,j
        i += 1
        j += 1
        self.energy = octopad[(i, j)]
    def __repr__(self) -> str:
        return f"{self.energy}"
    def get_neighbors(self):
        i = self.i
        j = self.j
        neighbors = [
            o for o in [
                Octopus(*p) for p in [
                    (i+1, j),
                    (i, j+1),
                    (i-1, j),
                    (i, j-1),
                    (i+1, j+1),
                    (i+1, j-1),
                    (i-1, j+1),
                    (i-1, j-1),
                ]
            ] if o
        ]
        return neighbors
    def step(self):
        self.energy += 1
    
class Octopi:
    def __init__(self):
        self.octopi = np.array([
            [
                Octopus(i,j) 
                for i in range(len(octopi))
            ] 
            for j in range(len(octopi))
        ])
    def __str__(self):
        out = '\n'.join([' '.join(map(str, row)) for row in self.octopi])
        return out.replace('0', color.RED + '0' + color.END)
    def __next__(self):
        this = self.octopi.copy()
        for row in this:
            for i in row:
                i.energy = i.energy + 1
                if i.energy > 9:
                    neigh = i.get_neighbors()
                    print(neigh)
                    for n in neigh:
                        n.energy = n.energy + 1
        for row in this:
            for i in row:
                if i.energy > 9:
                    i.energy = 0


octopi = Octopi()
# print(octopi)
# octopus = octopi.octopi[(0,0)]
# print(octopus.get_neighbors())

# %%
next(octopi)
print(octopi)

#%%
gen = iterate([3,4,5])
# %%
for i in range(10):
    print(next(gen))
# %%
