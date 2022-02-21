#%%

import numpy as np
from treelib import Node, Tree

with open('testinput') as f:
    cave = np.array([
        [int(i) for i in r]
        for r in f.read().splitlines()
    ])



def pad(arr):
    arrPad = np.zeros(tuple(
        s+2 for s in arr.shape
    )).astype(int)
    arrPad[1:-1, 1:-1] = arr
    return arrPad

def get_neighbors(p, arr):
    i,j = p
    I = i+1
    J = j+1
    arrPad = pad(arr)
    return {
        (p[0]-1,p[1]-1): arrPad[p] 
        for p in [
            # (I-1,J),
            # (I,J-1),
            (I+1,J), # only right
            (I,J+1)  # or down
        ] if arrPad[p] > 0
    }

tid = 't'

def get_ancestors(n: Node):
    ancestors = []
    pred = n.predecessor(tid)
    while pred:
        ancestors.append(pred)
        pred = tree.get_node(pred).predecessor(tid)
    return ancestors

tree = Tree(identifier=tid)
tree.create_node('1', '0-0*0@1')

M,N = cave.shape
i,j = 0,0
p = 0
def add_leaves(node = tree['0-0*0@1']):
    global p
    if (i,j) != (M-1, N-1):
        neighbors = get_neighbors(tuple([int(x) for x in node.identifier.split('*')[0].split('-')]), cave)
        for (k,v) in neighbors.items():
            if v == min(neighbors.values()):
                n = tree.create_node(
                    f'{v}, {k}', 
                    identifier = f'{k[0]}-{k[1]}*{p}@{v}', 
                    parent = node
                )
                p += 1
                add_leaves(n)

add_leaves()

tree.show()

for l in tree.leaves():
    ancs = get_ancestors(l)
    print(sum([int(a.split('@')[-1]) for a in ancs]) -1)


