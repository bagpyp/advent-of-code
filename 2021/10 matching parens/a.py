#%%

with open('input') as f:
    navsys = f.read().splitlines()

opens = '[{(<'
closes = ']})>'
pairs = ['[]','{}','()','<>']
match = {
    '[': ']', '{': '}', '(': ')', '<': '>',
    ']': '[', '}': '{', ')': '(', '>': '<'
}
scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

# {([(<{}[<>[]}>{[]{[(<()>
# {([(<[{{[(
# }>]])>

stacks = []
bad_closes = []

for line in navsys:
    stack = []
    for char in line:
        if char in opens:
            stack.append(char)
        elif char in closes:
            got = stack.pop()
            if got + char not in pairs:
                expected = match[got]
                bad_close = (char, expected)
                bad_closes.append(bad_close)
                print(f'{line} - Expected {expected}, but found {char} instead.')
    stack = ''.join(stack)
    stacks.append(stack)
    

from pprint import pprint
pprint(stacks)
pprint(bad_closes)

sum([scores[bc[0]] for bc in bad_closes])
# %%
