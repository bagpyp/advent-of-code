#%%

# build ops
with open('testinput') as f:
    ops = [
        (
            i,
            (
                l.split(' ')[0][0],
                int(l.split(' ')[1])
            )
        )
            for i,l in enumerate(
                f.read().split('\n')
            )
    ]

# %%

done = []
acc = 0

i,(op,val) = ops[0]
while True:
    if op == 'n':
        done.append(i)
        if len(done) != len(set(done)):
            break
        i,(op,val) = ops[i+1]
    elif op == 'j':
        done.append(i)
        if len(done) != len(set(done)):
            break
        i,(op,val) = ops[i+val]
    elif op == 'a':
        done.append(i)
        if len(done) != len(set(done)):
            break
        acc += val
        i,(op,val) = ops[i+1]
print(acc)
