#%%

from itertools import product
from re import X

x1,x2,y1,y2 = 102,157,-146,-90

def isInTargetArea(p):
  x,y = p
  return x >= x1 and x <= x2 and y >= y1 and y <= y2

def findXvs():
  xv = 0 
  while xv**2 + xv <= 2*x1:
    xv += 1
  min = xv
  xv = 0
  while xv**2 + xv <= 2*x2:
    xv += 1
  max = xv
  return list(range(min,max))
  

def checkPath(v):
  vx,vy = v
  path = [(0,0)]
  while path[-1][1] > y1:
    newX = path[-1][0] + max(0, vx - len(path))
    newY = path[-1][1] + (vy -len(path))
    path.append((newX,newY))

  return isInTargetArea(path[-1]), path

heights = []
for xv in findXvs():
  for yv in range(1000):
    hitsTarget,path = checkPath((xv,yv))
    if hitsTarget:
      print(xv,yv)
      heights.append(max([p[1] for p in path]))

print(max(heights))