#%%

from a import *

for l in lines:
    paper = fold(l,paper)

print(str(paper).replace('0',' '))

# [[13 13 74 13 65 21]
#  [96        8      ]
#  [25       12      ]
#  [    7 29         ]
#  [                 ]
#  [41  1 51 21  6 73]
#  [ 7     2       36]
#  [24    33       33]
#  [43             92]
#  [                 ]
#  [ 6  1  9 2  55 86]
#  [ 3        6      ]
#  [47       4  86   ]
#  [   2  19        3]
#  [                 ]
#  [    2 39 34  8   ]
#  [ 8             36]
#  [ 1             14]
#  [    7       49   ]
#  [                 ]
#  [   39 4  56 2    ]
#  [14             84]
#  [47       47    47]
#  [   52     8 76 38]
#  [                 ]
#  [            38   ]
#  [               44]
#  [55             5 ]
#  [33 33 38 38 51   ]
#  [                 ]
#  [5  21  6 16  7 37]
#  [87       33      ]
#  [46       85      ]
#  [    6 15         ]
#  [                 ]
#  [25 66 48  8 13 28]
#  [ 2    35       34]
#  [17    52       39]
#  [   13    39 14   ]
#  [                 ]]