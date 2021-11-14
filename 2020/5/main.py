#%%
with open('input') as f:
    seats = [
        (
            s[:7].replace('F','0').replace('B','1'),
            s[7:].replace('L','0').replace('R','1')
        ) for s in f.read().split('\n')
    ]
    # ..., ('FBBFFBF', 'LLR')] ->
    # ..., ('0110010', '001')]

# it's binary!
ids = [8*int(s[0],2) + int(s[1],2) for s in seats]
# >>> int('111', 2)
# 7    

# part 1
print(max(ids))

# part 2
for n in range(min(ids),max(ids)+1):
    if n not in ids:
        print(n)
# %%
