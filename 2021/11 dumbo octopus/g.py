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

with open('input') as f:
    octopi = np.array([
        [int(i) for i in list(j)] 
        for j in f.read().split()
    ])
h, w = octopi.shape

class Octopus:
    def __init__(self, i, j, energy) -> None:
        self.position = (i, j)
        self.energy = energy
    def __repr__(self) -> str:
        return self.energy
    def __str__(self) -> str:
        return str(self.energy)
    def get_neighbors(self):
        i, j = self.position
        neighbors = [(i+1, j),
                    (i, j+1),
                    (i-1, j),
                    (i, j-1),
                    (i+1, j+1),
                    (i+1, j-1),
                    (i-1, j+1),
                    (i-1, j-1)]
        neighbors = [n for n in neighbors 
            if 0 <= n[0] < h and 0 <= n[1] < w]
        return neighbors
    
class Octopi:
    def __init__(self, octopi):
        self.octopi = np.array([
            [
                Octopus(i, j, octopi[i,j]) 
                for j in range(len(octopi))
            ] 
            for i in range(len(octopi[0]))
        ])
        self.total_flashes = 0
    def __getitem__(self, pos):
        return self.octopi[pos[0], pos[1]]
    def __str__(self):
        out = '\n'.join([' '.join(map(str, row)) for row in self.octopi])
        return out.replace('0', color.RED + '0' + color.END)
    def get_neighbors(self, i, j):
        neighbors = self.octopi[i,j].get_neighbors()
        return [self.octopi[n[0],n[1]] for n in neighbors]
    def incr_neighbors(self, i, j):
        neighbors = self.get_neighbors(i,j)
        for n in neighbors:
            n.energy += 1
            if n.energy == 10:
                self.total_flashes += 1
                i,j = n.position
                self.incr_neighbors(i,j)
    def __next__(self):
        for row in self.octopi:
            for o in row:
                o.energy += 1
                if o.energy == 10:
                    self.total_flashes += 1
                    i,j = o.position
                    self.incr_neighbors(i,j)
        for row in self.octopi:
            for i in row:
                if i.energy > 9:
                    i.energy = 0
    def sum(self):
        return sum(
            [i.energy for row in self.octopi for i in row]
        )


O = Octopi(octopi)

# for i in range(100 + 1):
#     print(O)
#     print(O.total_flashes)
#     next(O)

from time import sleep
from IPython.display import clear_output
print(O)
sleep(.1)
while True:
    next(O)
    print(O)
    sleep(.1)
    clear_output(wait=True)
    if O.sum() == 0:
        break

# %%

# %%
