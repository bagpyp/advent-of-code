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
    # z is aim
    z = 0
    def move(self, direction, units):
        if direction == 'f':
            self.x += units
            self.y += self.z * units
        elif direction == 'd':
            self.z += units
        elif direction == 'u':
            self.z -= units
    def position(self):
        return self.x * self.y

sub = Submarine()

for c in course:
    sub.move(*c)

print(sub.position())
        
# %%
