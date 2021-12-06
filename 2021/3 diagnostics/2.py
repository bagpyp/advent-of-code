#%%

from os import X_OK
import numpy as np
import pandas as pd
import string

with open('input') as f:
    report = np.array([
        [int(ll) for ll in list(l)] 
        for l in f.read().splitlines()
    ])

def makeGamma(bitReport):
    return np.array([
        int(sum(arr)>=arr.size/2) 
        for arr in bitReport.T
    ])

gamma = makeGamma(report)

df = pd.DataFrame(
    report, 
    columns=list(
        string.axscii_lowercase[:gamma.size]
    )
)

i = 0
while len(df) > 1:
    col = df.columns[i]
    df = df[df[col]==gamma[i]]
    i += 1
    gamma = makeGamma(df.values)

oxygen = int(''.join([
    str(x) 
    for x in df.iloc[0].values
]),2)

df = pd.DataFrame(
    report, 
    columns=list(
        string.ascii_lowercase[:gamma.size]
    )
)

gamma = makeGamma(report)

i = 0
while len(df) > 1:
    col = df.columns[i]
    df = df[df[col]!=gamma[i]]
    i += 1
    gamma = makeGamma(df.values)

c02 = int(''.join([
    str(x) 
    for x in df.iloc[0].values
]),2)

print(oxygen * c02)
# %%

# %%
