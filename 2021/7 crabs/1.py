#%%

test = False

if test:
    poss = [16,1,2,0,4,2,7,1,2,14]
else:
    with open('input') as f:
        poss = [
            int(p) for p in 
            f.read().split(',')
        ]

fuel_costs = []
for pos in poss:
    fuel_cost = 0
    for otherPos in [p for p in poss if p != pos]:
        fuel_cost += abs(pos-otherPos)
    fuel_costs.append(fuel_cost)

print(min(fuel_costs))

# %%
