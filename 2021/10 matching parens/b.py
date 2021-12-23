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
points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

# {([(<{}[<>[]}>{[]{[(<()>
# {([(<[{{[(
# }>]])>

incomplete_stacks = []


for line in navsys:

    line_incomplete = True
    stack = []
    for char in line:
        if char in opens:
            stack.append(char)
        elif char in closes:
            got = stack.pop()
            if got + char not in pairs:
                expected = match[got]

                line_incomplete = False
                # print(f'{line} - Expected {expected}, but found {char} instead.')
    stack = ''.join(stack)
    if line_incomplete:
        incomplete_stacks.append(stack)

scores = []
for istack in incomplete_stacks:
    score = 0
    for char in istack[-1::-1]:
        score *= 5
        score += points[match[char]]
    scores.append(score)

print(sorted(scores)[int(len(scores)/2)])



# %%
