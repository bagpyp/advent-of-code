#%%
import numpy as np

test = False
fname = ['input','testinput'][test]
with open(fname) as f:
    notes = [
        [[
            ''.join(s)
            for s in l.split(' | ')[i].split()
        ] for i in (0, 1)]
        for l in f.read().splitlines()
    ]

with open('testoutput') as f:
    decoded_outputs = [
        l.split(': ') 
        for l in f.read().splitlines()
    ]

chars = 'abcdefg'

template = """\
  aaaa  
b      c
b      c
  dddd  
e      f
e      f
  gggg   \
"""

def display_raw(raw: str) -> str:
    # 'abcdef' -> '1111110'
    display = [0] * 7
    for s in raw:
        display[chars.index(s)] = 1
    return ''.join([str(d) for d in display])

def display_digital(raw: str) -> str:
    digital_display = template
    for char in chars:
        if char not in raw:
            digital_display = digital_display.replace(char, '')
    return digital_display.upper()

def get_signal(raw_display: str) -> str:
    # '0101010' -> 'bdf'
    signal = ''
    for i,bit in enumerate(raw_display):
        if bit == '1':
            signal += chars[i]
    return signal


normal = {
    'abcdefg': 8,
    'abcdfg': 9,
    'abcefg': 0,
    'abdefg': 6,
    'abdfg': 5,
    'acdeg': 2,
    'acdfg': 3,
    'acf': 7,
    'bcdf': 4,
    'cf': 1
}

class Signal:
    def __init__(self, raw: str) -> None:
        # 'abcdefg'
        self.raw = raw
        # '1111111'
        self.raw_display = display_raw(raw)
        #   AAAA  \nB      C\nB    ...
        self.digital_display = display_digital(raw)
        self.value = -1
    def __sub__(self, other):
        return ''.join([char for char in self.raw if char not in other.raw])
    def __repr__(self):
        return f'{self.raw}\n{self.raw_display}\n{self.digital_display}\n{self.value}\n'
    def is_subset(self, other):
        return all([char in other.raw for char in self.raw])
    def intersection(self, other):
        return [char for char in self.raw if char in other.raw]
    
    
class SignalGroup:
    def __init__(self, note) -> None:
        self.signals = [
            Signal(n) for n in note[0]
        ]
        self.proofs = note[1]
        self.matrix = np.array([
            [
                int(ss) for ss in s.raw_display] 
                for s in self.signals
            ])
        self.map = {char:'' for char in chars}
        self.row_sums = [sum(r) for r in self.matrix]
        self.col_sums = [sum(c) for c in self.matrix.T]
        self.decoded_signals = [-1] * 4
    def get_signal(self, val: int) -> Signal:
        return self.signals[[s.value for s in self.signals].index(val)]
    def get_signals_of_len(self, len: int) -> list[Signal]:
        signals = []
        for i,row_sum in enumerate(self.row_sums):
            if row_sum == len and self.signals[i].value < 0:
                signals.append(self.signals[i])
        return signals
    def __repr__(self):
        return f"{self.map}\n{[s.value for s in self.signals]}\n{self.matrix}\n"
    def decode(self):
        # for char, col_sum in {
        #     'f':9,
        #     'e':4,
        #     'b':6
        # }.items():
        #     self.map[char] = chars[self.col_sums.index(col_sum)]
        for val, row_sum in {
            1:2,
            7:3,
            4:4,
            8:7
        }.items():
            self.signals[self.row_sums.index(row_sum)].value = val
        self.map['a'] = self.get_signal(7) - self.get_signal(1)
        [s for s in self.get_signals_of_len(5) if self.get_signal(1).is_subset(s)][0].value = 3
        [s for s in self.get_signals_of_len(5) if len(self.get_signal(4).intersection(s)) == 2][0].value = 2
        self.get_signals_of_len(5)[0].value = 5
        self.map['c'] = self.get_signal(1).intersection(self.get_signal(2))[0]
        self.map['f'] = self.get_signal(1).intersection(self.get_signal(5))[0]
        [s for s in self.get_signals_of_len(6) if len(self.get_signal(7).intersection(s)) == 2][0].value = 6
        [s for s in self.get_signals_of_len(6) if self.get_signal(5).is_subset(s)][0].value = 9
        self.get_signals_of_len(6)[0].value = 0
        self.map['e'] = self.get_signal(8) - self.get_signal(9)
        self.map['d'] = self.get_signal(9) - self.get_signal(0)
        self.map['b'] = self.get_signal(4) - self.get_signal(3)
        self.map['g'] = [char for char in chars if char not in self.map.values()][0]
        self.map = {v:k for k,v in self.map.items()}
        for i, proof in enumerate(self.proofs):
            self.decoded_signals[i] = normal[''.join(sorted([self.map[char] for char in proof]))]
        
signals = []
for note in notes:
    sg = SignalGroup(note)
    sg.decode()
    signals.append(int(''.join([str(n) for n in sg.decoded_signals])))

print(sum(signals))

# %%

# %%
