#%%

from treelib import Node, Tree

with open('testinput') as f:
    lines = f.read().splitlines()

vertices = []
for line in lines:
    vertices.extend(line.split('-'))
vertices = list(set(vertices))

graph = {v:[] for v in vertices}

for line in lines:
    a,b = line.split('-')
    graph[a] += [b]
    graph[b] += [a]

for v in vertices:
    if 'start' in graph[v]:
        graph[v].pop(graph[v].index('start'))

graph['end'] = []

# {'A': ['c', 'b', 'end'],
#  'd': ['b'],
#  'start': ['A', 'b'],
#  'c': ['A'],
#  'b': ['A', 'd', 'end'],
#  'end': []}

tid = 'tid'

def get_ancestors(n: Node):
    ancestors = []
    pred = n.predecessor(tid)
    while pred:
        ancestors.append(pred)
        pred = tree.get_node(pred).predecessor(tid)
    return ancestors
    
def add_leaves(i):
    added = 0
    for j,leaf in enumerate(tree.leaves()):
        parent = leaf.identifier
        possible_children = graph[parent.split('-')[-1]]
        for pc in possible_children:
            if pc == pc.upper() or pc not in [p.split('-')[-1] for p in get_ancestors(leaf)]:
                tree.create_node(pc, f"{i+1}-{j}-{pc}", parent=parent)
                added = 1
    return added

tree = Tree(identifier=tid)
tree.create_node('start', '0-0-start')

# tree.show()



i = 1
while i > 0:
    i = add_leaves(i) * (i+1)
    # tree.show()

tree.show()
print([l.tag for l in tree.leaves()].count('end'))

# %%
