#%%
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'({self.x},{self.y})'

class Line:
    def __init__(self, p1, p2):
        p1,p2 = sorted(
            sorted(
                [p1,p2], 
                key = lambda p: p.y
            ), 
            key = lambda p: p.x
        )
        self.p1 = p1
        self.p2 = p2
        try:
            self.slope = (p2.y - p1.y)/(p2.x - p1.x)
        except ZeroDivisionError:
            self.slope = None
        self.points = self.fill_in()
    def __repr__(self):
        return f'{self.p1} -> {self.p2}: {self.points}'
    def fill_in(line):
        a,b = line.p1, line.p2
        points = [a]
        if line.slope == None:
            for i in range(b.y - a.y):
                points.append(Point(points[-1].x, points[-1].y + 1))
        else:
            for i in range(b.x - a.x):
                points.append(
                    Point(
                        points[-1].x+1, 
                        int(points[-1].y+1 * line.slope)
                    )
                )
        return points
        
if __name__ == '__main__':
    
    import numpy as np
    from parse import compile
    import matplotlib.pyplot as plt

    p = compile('{x1:d},{y1:d} -> {x2:d},{y2:d}')
    with open ('input') as f:
        point_pairs = [p.parse(l).named for l in f.read().splitlines()]

    lines = [
        Line(
            Point(
                pp['x1'], pp['y1']
            ),
            Point(
                pp['x2'], pp['y2']
            )        
        ) for pp in point_pairs
    ]

    field = np.zeros(
        (
            max([l.p2.x for l in lines]) + 1,
            max([l.p2.y for l in lines]) + 1
        )
    ).astype(int)

    for l in lines:
        for p in l.points:
            field[p.y, p.x] += 1

    plt.imshow(field)

    print(sum(sum(field >= 2)))



# %%