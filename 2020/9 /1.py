#%%

with open('input') as f:
    xmas = [int(l) for l in f.readlines()]

preamble_length = 25

for (i, number) in enumerate(xmas[preamble_length:]):
    i = i + preamble_length
    preamble = xmas[i-preamble_length : i+1]
    L = []
    for j in preamble:
        for k in preamble:
            if j != k:
                L.append(j + k)
    if number not in L:
        break

# number is the first invalid elt in xmas (127)

for i,val in enumerate(xmas):
    if val != number:
        acc = val
        j = i
        while acc <= number:
            j += 1
            acc += xmas[j]
            if acc == number:
                spread = xmas[i:j]

print(max(spread) + min(spread))

        

        





# %%
