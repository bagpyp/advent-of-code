#%%

from datetime import datetime as dt

def makeOps():
    with open('input') as f:
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
    return ops

def do(ops):
    acc = 0
    i,(op,val) = ops[0]
    a = dt.now()
    while ((dt.now()-a).seconds < .1):
        if op == 'n':
            try:
                i,(op,val) = ops[i+1]
            except IndexError:
                print(acc)
                break
        elif op == 'j':
            try:
                i,(op,val) = ops[i+val]
            except IndexError:
                print(acc)
                break
        elif op == 'a':
            try:
                acc += val
                i,(op,val) = ops[i+1]
            except IndexError:
                print(acc)
                break

#get a list of naughty ops
switched = []

done = []
acc = 0
ops = makeOps()
i,(op,val) = ops[0]
while True:
    if op == 'n':
        if i+1 in done:
            switched.append(i)
            i,(op,val) = ops[i+val]
        else:
            try:
                done.append(i)
                i,(op,val) = ops[i+1]
            except IndexError:
                break
    elif op == 'j':
        done.append(i)
        if i+val in done:
            switched.append(i)
            i,(op,val) = ops[i+1]

        else:
            try:
                i,(op,val) = ops[i+val]
            except IndexError:
                break
    elif op == 'a':
        done.append(i)
        acc += val
        try:
            i,(op,val) = ops[i+1]
        except IndexError:
            break


def swap(ops,s):
    badOp = ops[s]
    newOp = (
        badOp[0],
        (
            'n' if badOp[1][0] == 'j' else 'n',
            badOp[1][1]
        )
    )
    ops = ops[:s] + [newOp] + ops[s+1:]
    return ops

for s in switched[-1::-1]:
    print(f'trying {s}')
    ops = makeOps()
    ops = swap(ops,s)
    do(ops)
    


# %%
