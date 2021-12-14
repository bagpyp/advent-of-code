#%%

test = True
fname = ['input','testinput'][test]
with open(fname) as f:
    notes = [
        [sorted([
            ''.join(sorted(s))
            for s in sorted(l.split(' | ')[i].split())
        ]) for i in (0, 1)]
        for l in f.read().splitlines()
    ]

with open('testoutput') as f:
    decoded_outputs = [
        l.split(': ') 
        for l in f.read().splitlines()
    ]

chars = 'abcdefg'

default = [
    '1110111',
    '0010010',
    '1011101',
    '1011011',
    '0111010',
    '1101011',
    '1101111',
    '1010010',
    '1111111',
    '1111011'
    ]

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
            digital_display = digital_display.replace(char, '.')
    return digital_display.upper()

def get_signal(raw_display: str) -> str:
    # '0101010' -> 'bdf'
    signal = ''
    for i,bit in enumerate(raw_display):
        if bit == '1':
            signal += chars[i]
    return signal


class Signal:
    def __init__(self, raw: str) -> None:
        self.raw = raw
        self.raw_display = display_raw(raw)
        self.digital_display = display_digital(raw)
    def __repr__(self):
        return f'{self.raw}\n{self.raw_display}\n{self.digital_display}\n'
    

# %%


