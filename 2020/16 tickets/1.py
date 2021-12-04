#%%
from parse import parse
from functools import reduce

my_ticket = [223,
        139,
        211,
        131,
        113,
        197,
        151,
        193,
        127,
        53,
        89,
        167,
        227,
        79,
        163,
        199,
        191,
        83,
        137,
        149]

with open('rules') as ruleFile:
    rules = [
        parse("{name}: {m1:d}-{M1:d} or {m2:d}-{M2:d}", r).named
        for r in ruleFile.read().splitlines()
    ]

with open('tickets') as ticketFile:
    tickets = [
        [int(tt) for tt in t.split(',')] 
        for t in ticketFile.read().splitlines()
    ]

vals = reduce(set.union,
    [
        set(range(
            rule['m1'], rule['M1']
        )).union(
            set(range(
                rule['m2'], rule['M2']
            ))
        )
        for rule in rules
    ]
)

invalid_vals = []
valid_tickets = []
for ticket in tickets:
    valid = True
    for t in ticket:
        if t not in vals:
            valid = False
            invalid_vals.append(t)
    if valid:
        valid_tickets.append(ticket)
    
# print(sum(invalid_vals))





# %%
