#%%

def get_io(test = False):
    fname = ['input','testinput'][test]
    with open(fname) as f:
        lines = f.read().splitlines()
        inputs, outputs = [
                [
                    ''.join(sorted(s))
                    for l in lines
                    for s in sorted(l.split(' | ')[i].split())
                ]
            for i in (0,1)
        ]
    return inputs, outputs

print(get_io(True))

if __name__ == '__main__':
    inputs, outputs = get_io()
    print(sum([len(o) in [2,3,4,7] for output in outputs for o in output]))
# %%



# %%
