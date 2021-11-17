#%%
with open('input') as f:
    passports = [dict([p.split(':') for p in pp]) for pp in [p.replace('\n',' ').split(' ') for p in f.read().split('\n\n')]]

keys = ['byr', 'cid', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
class Passport:
    ecls = 'amb blu brn gry grn hzl oth'.split(' ')
    def __init__(self, passport):
        self.eyr = passport.get('eyr')
        self.hgt = passport.get('hgt')
        self.ecl = passport.get('ecl')
        self.byr = passport.get('byr')
        self.iyr = passport.get('iyr')
        self.pid = passport.get('pid')
        self.hcl = passport.get('hcl')
        self.cid = passport.get('cid')
        self.numKeys = len(set(passport.keys()))   
        self.hasCid = 'cid' in passport
    def isValid(self): 
        valid = True
        while valid:
            valid = valid and ((self.numKeys == 8) or ((self.numKeys == 7) and (self.cid is None)))
            valid = valid and ((self.byr is not None) and (
                ((len(self.byr) == 4) and 
                (1920 <= int(self.byr) <= 2002))
            ))
            valid = valid and ((self.ecl is not None) and (
                self.ecl in self.ecls
            ))
            valid = valid and ((self.eyr is not None) and (
                ((len(self.eyr) == 4) and 
                (2020 <= int(self.eyr) <= 2030))
            ))
            valid = valid and ((self.hcl is not None) and (
                len(self.hcl) == 7 
                    and (self.hcl[0] == '#')
                    and (all([ch in '0123456789abcdef' for ch in self.hcl[1:]]))
            ))
            preValid = ((self.hgt is not None) and (
                (len(self.hgt) > 2) and (self.hgt[-2:] in ['cm','in'])
            ))
            if preValid and self.hgt[-2:] == 'cm':
                valid = valid and (150 <= int(self.hgt[:-2]) <= 193)
            elif preValid and self.hgt[-2:] == 'in':
                valid = valid and (59 <= int(self.hgt[:-2]) <= 76)
            else: 
                return False
            valid = valid and ((self.iyr is not None) and (
                ((len(self.iyr) == 4) and 
                (2010 <= int(self.iyr) <= 2020))
            ))
            valid = valid and ((self.pid is not None) and (
                (len(self.pid) == 9) and int(self.pid.lstrip('0'))
            ))
            return valid > 0
        return False
        
print(sum([Passport(passport).isValid() for passport in passports]))        

# %%
