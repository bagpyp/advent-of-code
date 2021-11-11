#%% build data


import numpy as np
from tqdm import tqdm

with open('input') as f:
    ruleStrings = f.read().split('\n')

rules = []
colors = []
for ruleString in tqdm(ruleStrings):
    split = ruleString.split(' bags contain ')
    color = split[0]
    colors.append(color)
    colorContains = split[1]
    contains = {}
    for cc in colorContains.split(', '):
        if colorContains != 'no other bags.':
            cc = cc.replace('bags', 'bag')
            cc = cc.replace('.','')
            cc = cc.replace(' bag','')

            contains.update({' '.join(cc.split(' ')[1:]):int(cc.split(' ')[0])})
    rules.append({'color':color, 'contains':contains})

# {'color': 'clear gold', 'contains': [{'dotted orange': 3}]},
# {'color': 'bright fuchsia', 'contains': []},
# {'color': 'dull maroon',
#  'contains': [{'posh green': 3},
#               {'shiny gold': 1},
#               {'light salmon': 5},
#               {'posh teal': 1}]},

data = []
for rule in rules:
    contains = rule['contains']
    counts = []
    for color in colors:
        counts.append((0,contains.get(color))[color in contains])
    data.append(counts)


#%%
arr = np.array(data)


# input = arr
# df = pd.DataFrame(data=arr, index=colors, columns=colors)
# print(df)
# array([[0, 0, 0, ..., 0, 0, 0],
#        [0, 0, 0, ..., 0, 0, 0],
#        [0, 0, 0, ..., 0, 0, 0],
#        ...,
#        [0, 0, 0, ..., 0, 0, 0],
#        [0, 0, 0, ..., 0, 0, 0],
#        [0, 0, 0, ..., 0, 0, 0]])

# arr = np.array(
#     [
#         [0,0,0,0,2,1,0,0,0],
#         [0,0,1,2,0,0,0,0,0],
#         [1,0,0,0,0,0,0,0,0],
#         [2,0,0,0,0,0,9,0,0],
#         [0,0,0,0,0,0,5,6,0],
#         [0,0,0,0,0,0,3,4,0],
#         [0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0],
#         [0,0,3,0,0,0,0,0,0]
#     ]
# )

# print(arr)
def reOrderArr(arr):
    N = len(arr)
    toCheck = list(range(N))
    newArr = np.zeros((N,N))
    swapped = []
    while len(swapped) < N:
        for i in toCheck.copy():
            rowSum = arr[i,toCheck].sum()
            if rowSum == 0:
                toSwap = toCheck.pop(toCheck.index(i))
                newArr = arr[swapped + [toSwap] + toCheck]
                swapped.append(toSwap)
        print(len(swapped))
    newArr = newArr[:,swapped]
    return newArr, swapped

arr, swapped = reOrderArr(arr)



# print(arr)

# df = df = pd.DataFrame(data=arr, index = [colors[i] for i in swapped], columns=[colors[i] for i in swapped])
# print(df)
def buildArr(arr):
    N = len(arr)
    num = 0

    oldArr = arr.copy()
    for i,r in tqdm(enumerate(arr)):
        for j,c in enumerate(r):
            if (i != j):
                x = arr[i][j]
                if x != 0:
                    # arr2 = arr.copy()
                    for k in range(N):
                        if arr[j][k] != 0:
                            
                            arr[i][k] += arr[j][k] * x
                    # diff = arr-arr2
                    # if diff.sum() != 0:
                    #     num += 1
                    #     print(f'STEP {num}--------------------------')
                    #     print('This is the output of the last step:')
                    #     print(arr2)
                    #     print(f'After inspecting row {i}, column {j} (and finding {x}) in the above array') 
                    #     print('I chose to add this to the above array\n',arr-arr2)
                    #     print(f'It should be {x} mulitiplied by the {j}th row of the matrix in the output of the last step')
                    #     print('That computation resulted in:\n',arr,'\n\n')
    return arr

arr = buildArr(arr)
# output = arr
# print(colors[swapped])
# df = pd.DataFrame(data=arr, index = [colors[i] for i in [7, 8, 5, 6, 4, 2, 3, 0, 1]], columns=[colors[i] for i in [7, 8, 5, 6, 4, 2, 3, 0, 1]])
# print(df)

# print(df.loc[colors, colors])

shinyGold = swapped.index(colors.index('shiny gold'))

print((arr[:,shinyGold]>0).sum(), arr[shinyGold,:].sum())
# %%
