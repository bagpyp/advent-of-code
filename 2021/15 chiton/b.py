#%%
from itertools import product
from IPython.display import clear_output
import matplotlib.pyplot as plt
from math import sqrt
import numpy as np

with open('input') as f:
    cave = np.array([
        [int(i) for i in r]
        for r in f.read().splitlines()
    ])

N = len(cave) - 1 # steps x and y to goal

class Node:
    def __init__(self, p, v, parent=None):
        self.parent = parent
        self.tag = f'{p[0]}-{p[1]}'
        self.p = p
        self.v = v
        self.g = 0
        self.h = sqrt(
            # euclidean to goal
            (N-p[0])**2 + (N-p[1])**2
        )
        self.visited = self.tag in CLOSE
    def compute_g(self):
        node = self
        g = node.v
        if node.parent:
            g += node.parent.g
        self.g = g
        return g
    def compute_f(self):
        f = self.h + self.compute_g()
        self.f = f
        return f
    def successors(self):
        i,j = self.p
        I,J = i+1,j+1
        pad = np.zeros(tuple(
            s+2 for s in cave.shape
        )).astype(int)
        pad[1:-1, 1:-1] = cave
        return [
            Node(
                (p[0]-1,p[1]-1), 
                pad[p]
            ) 
            for p in [
                (I-1,J),
                (I,J-1),
                (I+1,J),
                (I,J+1),
                # (I+1,J+1),
                # (I-1,J+1),
                # (I+1,J-1),
                # (I-1,J-1)
            ] if pad[p] > 0
        ]
    def display(self):
        current = self
        display = np.zeros((N+1, N+1))
        display[current.p] = 1
        score = current.v
        while current.parent:
            display[current.parent.p] = 1
            score += current.parent.v
            current = current.parent
        clear_output(wait=True)
        plt.imshow(display)
        plt.pause(.00001)
        print(score)

""" 
A*
"""
CLOSE = []
OPEN = [Node((0,0),0)]
i = 0
while OPEN:
    i += 1
    current = OPEN.pop(OPEN.index(
            min(OPEN, key=lambda n: n.compute_f())
        ))
    if current.p == (N,N):
        current.display()
        break
    else:
        current.visited = True
        CLOSE.append(current.tag)
    for n in current.successors():
        if not n.visited:
            tentative_g = current.compute_g() + n.v
            if n.g == 0 or tentative_g < n.g:
                n.parent = current
                n.g = tentative_g
                if n.tag not in [o.tag for o in OPEN]:
                    OPEN.append(n)
    if i%5000 == 0:
        current.display()