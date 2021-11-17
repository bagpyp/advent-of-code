#%%

import time

a = time.perf_counter()

class Password:
    def __init__(self, string):
        _pieces = string.split(' ')
        self.min, self.max = list(map(int,_pieces[0].split('-')))
        self.char = _pieces[1][0]
        self.pwd = _pieces[2][:-1]
    def isValid(self):
        
        try:
            return ((self.min <= len(self.pwd)) 
                    and ((self.pwd[self.min-1] == self.char)) 
                ^ ((self.max <= len(self.pwd)) 
                    and (self.pwd[self.max-1] == self.char)))
        except IndexError as e:
            print(self.min, self.max, self.pwd, self.char)
            print(e)
            return False
with open('input') as f:
    passwords = [Password(line) for line in f]

print(sum([p.isValid() for p in passwords]))

b = time.perf_counter()

print(f'took {(b-a) * 1e3}ms')


#%%
