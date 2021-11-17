#%%

class console:
    def __init__(self, puzzle_input):

        self.acc = 0
        self.prog = [
            (line.split(" ")[0], int(line.split(" ")[1])) for line in puzzle_input
        ]
        self.eip = 0
        self.executed_insts = set()

    def run(self):

        while self.eip not in self.executed_insts:
            self.executed_insts.add(self.eip)
            op, arg = self.prog[self.eip]
            if op == "acc":
                self.acc += arg
                self.eip += 1
            elif op == "jmp":
                self.eip += arg
            elif op == "nop":
                self.eip += 1
            else:
                raise ValueError(f"Invalid op code: [{self.eip}] {self.prog}")
            if self.eip == len(self.prog):
                return 0
        return -1


with open('input', "r") as f:
    data = f.read().strip().split("\n")

c = console(data)
c.run()
print(f"Part 1: {c.acc}")

for i in range(len(data)):
    if "acc" in data[i]:
        continue
    elif "jmp" in data[i]:
        mod = data[i].replace("jmp", "nop")
    elif "nop" in data[i]:
        mod = data[i].replace("nop", "jmp")
    else:
        raise ValueError(f"Invalid op code: [{c.eip}] {c.prog}")
    c = console(data[:i] + [mod] + data[i + 1 :])
    if c.run() == 0:
        print(f"Part 2: {c.acc}")
        break
# %%
