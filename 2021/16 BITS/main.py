#%%
import pprint 
from treelib import Node, Tree
import os


parents = [-1]
packets = []
pointer = 0

class Packet:
  
  id: int = 0
  parent: int = -1
  version: int
  packetType: str

  subPacketLengthType: str

  lengthOfSubPackets: int = 0
  subPacketsLengthCurrent: int = 0

  length: int = 0
  numberOfSubPackets: int = 0
  subPacketsCurrent: int = 0

  value: int 
  operatorType: int = -1
  startedAt: int = 0

  def __init__(self, buffer):
    global pointer
    global packets
    global parents

    self.id = len(packets)
  
    if self.id != 0:
      parentsCopy = parents.copy()
      for p in parents[-1:0:-1]:
        parent = getPacketById(p)
        if parent.subPacketLengthType == 'nextFifteenDetermineLengthOfSubPackets':
          if parent.subPacketsLengthCurrent == parent.lengthOfSubPackets:
            grandparent = getPacketById(getPacketById(parentsCopy.pop()).id)
            uncles = getPacketChildren(grandparent.id)
            grandparent.setsubPacketsLengthCurrent(sum([u.length for u in uncles]) + grandparent.length)
            
        elif parent.subPacketLengthType == 'nextElevenDetermineNumberOfSubPackets':
          if parent.subPacketsCurrent == parent.numberOfSubPackets:
            grandparent = getPacketById(getPacketById(parentsCopy.pop()).id)
            uncles = getPacketChildren(grandparent.id)
            grandparent.setsubPacketsCurrent(len(uncles))


      parents = parentsCopy

    self.parent = parents[-1]
    
    self.startedAt = pointer

    self.version = int(buffer[:3],2)
    buffer = buffer[3:]
    pointer += 3
    self.packetType = packetType(buffer[:3])
    maybeOperatorType = int(buffer[:3],2)
    buffer = buffer[3:]
    pointer += 3
    if self.packetType == 'operator':
      parents.append(self.id)
      self.operatorType = maybeOperatorType
      self.subPacketLengthType = subPacketLengthType(buffer[0])
      buffer = buffer[1:]
      pointer += 1
      if self.subPacketLengthType == 'nextFifteenDetermineLengthOfSubPackets':
        self.lengthOfSubPackets = int(buffer[:15],2)
        buffer = buffer[15:]
        pointer += 15
        
      elif self.subPacketLengthType == 'nextElevenDetermineNumberOfSubPackets':
        self.numberOfSubPackets = int(buffer[:11],2)
        buffer = buffer[11:]
        pointer += 11
      self.length = pointer - self.startedAt

    elif self.packetType == 'literalValue':
      valueBits = ''
      groupStart = buffer[0]
      while int(groupStart) == 1:
        buffer = buffer[1:]
        pointer += 1
        valueBits += buffer[:4]
        buffer = buffer[4:]
        pointer += 4
        groupStart = buffer[0]
      valueBits += buffer[1:5]
      buffer = buffer[5:]
      pointer += 5

      self.value = int(valueBits,2)
      self.length = pointer - self.startedAt

    if self.id != 0:
      parent = getPacketById(self.parent)
      if parent.subPacketLengthType == 'nextFifteenDetermineLengthOfSubPackets':

        parent.setsubPacketsLengthCurrent(parent.subPacketsLengthCurrent + self.length)
        # if parent.subPacketsLengthCurrent == parent.lengthOfSubPackets:
        #   parents.pop()
      elif parent.subPacketLengthType == 'nextElevenDetermineNumberOfSubPackets':
        parent.setsubPacketsCurrent(parent.subPacketsCurrent + 1)
        # if parent.subPacketsCurrent == parent.numberOfSubPackets:
        #   parents.pop()




  def __repr__(self):
    if self.packetType == 'operator':
      return f'{self.id},{self.parent},op,{operatorMap[self.operatorType].__name__}'
    else:
      return f'{self.id},{self.parent},val,{self.value}'
  
  def setsubPacketsLengthCurrent(self,val):
    self.subPacketsLengthCurrent = val
  
  def setsubPacketsCurrent(self,val):
    self.subPacketsCurrent = val

def getPacketById(id: int) -> Packet:
  return [p for p in packets if p.id == id][0]

def getPacketChildren(id: int):
  return [p for p in packets if p.parent == id]

def packetType(XXX):
    if int(XXX,2) == 4:
        return 'literalValue'
    else:
        return 'operator'

def subPacketLengthType(X):
    if int(X) == 0:
      return 'nextFifteenDetermineLengthOfSubPackets'
    else: 
      return 'nextElevenDetermineNumberOfSubPackets'

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

def sumCustom(*args):
  if len(args) == 1:
    return args[0]
  else:
    return sum(args)

def minCustom(*args):
  if len(args) == 1:
    return args[0]
  else:
    return min(*args)

def maxCustom(*args):
  if len(args) == 1:
    return args[0]
  else:
    return max(*args)

def prod(*args):
  res = 1
  for a in args:
    res *= a
  return res

def greaterThan(a,b):
  return int(a > b)

def lessThan(a,b):
  return int(a < b)

def equalTo(a,b):
  return int(a == b)

operatorMap = {
  0: sumCustom,
  1: prod,
  2: minCustom,
  3: maxCustom,
  5: greaterThan,
  6: lessThan,
  7: equalTo
}

operatorNameMap = {
  'sumCustom':sumCustom,
  'prod':prod,
  'minCustom':minCustom,
  'maxCustom':maxCustom,
  'greaterThan':greaterThan,
  'lessThan':lessThan,
  'equalTo':equalTo
}

class Node:
  id = 0
  parent = -1
  type = ''
  isReducable = False
  def __init__(self,repr):
    stuff = repr.split(',')
    self.id = int(stuff[0])
    self.parent = int(stuff[1])
    if stuff[2] == 'op':
      self.type = 'op'
      self.op = operatorNameMap[stuff[3]]
    else: 
      self.val = int(stuff[3])
      self.type = 'val'
  def __repr__(self) -> str:
      return str({k:v for k,v in self.__dict__.items() if k != 'children'})
  def setChildren(self, children):
    self.children = children
  def setIsReducable(self, isReducable):
    self.isReducable = isReducable

def removeNodes(nodes, ids):
  nodesCopy = nodes.copy()
  return [n for n in nodesCopy if n.id not in ids]


if __name__ == '__main__':

  with open('testinput') as f:
    streams = f.read().split('\n')

  with open('input') as f:
    streams.append(f.read())

  for stream in streams[-1:]:
    parents = [-1]
    packets = []
    pointer = 0
    packetString = bits(stream)
    
    while len(packetString[pointer:]) > 11:
      packets.append(Packet(packetString[pointer:]))

    nodes = [Node(str(p)) for p in packets]
  
    def tag(node: Node):
      if node.type == 'op':
        return f'{node.id}: {node.op.__name__}'
      else:
        return f'{node.id}: {node.val}'

    nodesLeft = len(nodes)
    tree = Tree()
    root = tree.create_node(tag(nodes[0]),nodes[0].id)
    nodesLeft -= 1
    while nodesLeft > 0:
      for leaf in tree.leaves():
        for node in nodes:
          if node.parent == leaf.identifier: 
            tree.create_node(tag(node), node.id, parent=leaf.identifier)
            nodesLeft -= 1
    with open('tree.txt','w') as t:
      t.write('')
    tree.save2file('tree.txt')


  # N = len(nodes)
  # while N > 1:
  #   for n in nodes:
  #     children = [nn for nn in nodes if nn.parent == n.id]
  #     n.setChildren(children)
  #     n.setIsReducable(len(children)>0 and all([c.type == 'val' for c in children]))
  #   leaves = [n for n in nodes if n.isReducable]
  #   for leaf in leaves:
  #     leafValue = leaf.op(*[c.val for c in leaf.children])
  #     newLeaf = Node(f'{leaf.id},{leaf.parent},val,{leafValue}')
  #     replacableLeaves = [c.id for c in leaf.children] + [leaf.id]
  #     nodes = removeNodes(nodes, replacableLeaves)
  #     nodes = nodes + [newLeaf]
  #   N = len(nodes)
  #   print(N)



# %%
