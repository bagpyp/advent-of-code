#%%

with open('input') as f:
    stream = f.read()

def bits(stream): 
    key = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
    }
    return ''.join([key[s] for s in stream])

# O4 > O1 > O5 > L6
a = '8A004A801A8002F478' # 16
# O3 > [ O > [L,L] , O > [L,L] ]
b = '620080001611562C8802118E34' # 12
# O3_ > [ O > [L,L] , O > [L,L] ]
c = 'C0015000016115A2E0802F182340' # 23
# O > O > O > [L,L,L,L,L]
d = 'A0016C880162017C3686B18A3D4780' # 31

def packetType(i):
    if int(i) == 4:
        return 'L'
    else:
        return 'O'
def packetListType(i):
    return 'n' if int(i) else 'd'



class Packet:
    v: int
    t: int
    lv: int
    lti: int
    numPackets: int
    lenPackets: int
    packets: list
    def __repr__(self):
        if self.t == 4:
            return f'{packetType(self.t)}v{self.v}'
        else:
            return f'{packetType(self.t)}v{self.v}_{packetListType(self.lti)} > {self.packets}'
    def __init__(self, bits, parent=None):
        self.parent = parent
        self.packets = []
        self.v = int(bits[:3], 2)
        self.t = int(bits[3:6], 2)
        self.lti = -1
        if self.t == 4:
            i, groups = 0, ''
            while int(bits[int(3+3 + 5*i)]):
                groups += bits[int(3+3 + 5*i) + 1 : int(3+3 + 5*i) + 5]
                i += 1
            groups += bits[int(3+3 + 5*i) + 1 : int(3+3 + 5*i) + 5]
            left_over = bits[int(3+3 + 5*i) + 5:]
            self.lv = int(groups, 2)
            self.parent.packets.append(Packet(left_over), parent = self.parent)
        else:
            self.lti = int(bits[6])
            if self.lti:

                self.numPackets = int(bits[3+3+1 : 3+3+1 + 11], 2)
                left_over = bits[3+3+1+11:]
                print(left_over, len(left_over))
                if len(left_over) >= 7:
                    self.packets.append(Packet(left_over, parent = self))
            else:
                self.lenPackets = int(bits[3+3+1 : 3+3+1 + 15], 2)
                left_over = bits[3+3+1 + 15:]
                print(left_over, len(left_over))
                if len(left_over) >= 7:
                    self.packets.append(Packet(bits[3+3+1 + 15 : 3+3+1 + 15 + self.lenPackets], parent = self))


ps = [Packet(bits(x)) for x in [d]]
