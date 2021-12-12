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
for pos in range(max(poss)):
    fuel_cost = 0
    for otherPos in poss:
        n = abs(pos-otherPos)
        additional_fuel_cost = int((n*(n+1))/2)
        fuel_cost += additional_fuel_cost

    fuel_costs.append(fuel_cost)

print(min(fuel_costs))

# %%
