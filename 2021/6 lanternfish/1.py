#%%
with open ('testinput') as f:
    input = [int(l) for l in f.read().split(',')]

class Fish:
    def __init__(self, timer: int = 8) -> None:
        self.timer = timer
    def __repr__(self) -> str:
        return str(self.timer)
    def wake_up(self):
        if self.timer < 7:
            self.timer = (self.timer - 1) % 7
        else:
            self.timer -= 1

class School:
    def __init__(self, fish: list[Fish]) -> None:
        self.fish = fish
    def __repr__(self) -> str:
        return str(self.fish)
    def cycle(self):
        bursters = [f.timer for f in self.fish].count(0)
        for f in self.fish:
            f.wake_up()
        self.fish.extend([Fish() for _ in range(bursters)])
    def count_fish(self):
        return len(self.fish)

school = School([Fish(i) for i in input])

if __name__ == '__main__':
    for _ in range(80):
        school.cycle()

    print(school.count_fish())
# %%
