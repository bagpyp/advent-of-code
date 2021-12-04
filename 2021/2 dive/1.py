#%%

with open('input') as f:
    course = [
        (l.split()[0][0],int(l.split()[1])) 
        for l in f.read().splitlines()
    ]

class Submarine:
    x = 0
    # y is depth
    y = 0
    def move(self, direction, units):
        if direction == 'f':
            self.x += units
        elif direction == 'd':
            self.y += units
        elif direction == 'u':
            self.y -= units
    def position(self):
        return self.x * self.y

sub = Submarine()

for c in course:
    sub.move(*c)

print(sub.position())
        
# %%
