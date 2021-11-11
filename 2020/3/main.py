#%%
with open('input') as f:
    treelines = f.read().split('\n')

top = treelines[0]
N = len(treelines)
M = len(top)

dx = 3
dy = 1

def treesFromSlope(slope):
    dx,dy = slope
    paths = []
    for x,t in enumerate(top):
        if x > 0:
            break
        if t == '#':
            continue
        trees = 0
        y = 0
        while y < N-1:
            x = (x + dx) % M
            y += dy
            trees += treelines[y][x] == '#'
        paths.append(trees)
    return paths[0]


print(treesFromSlope((dx,dy)))

res = 1
for slope in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
    res *= treesFromSlope(slope)
    print(res)
#%%
