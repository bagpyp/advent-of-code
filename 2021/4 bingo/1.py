#%% 
import numpy as np
from numpy.lib.function_base import bartlett

with open('testinput') as f:
    input = f.read().split('\n\n')

draws, boards = \
    [
        int(d) 
        for d in input[0].split(',')
    ], \
    [
        [
            [
                int(bbb) 
                for bbb in bb.split()
            ]
            for bb in b.split('\n')
        ]
        for b in input[1:]
    ]

class Board:
    def __init__(self,arr):
        self.card = np.array(arr)
        self.cardState = np.zeros(self.card.shape).astype(int)
    def __repr__(self):
        return '\n'.join([str(self.card),str(self.cardState)]) + '\n'
    def updateState(self,draw):
        I, J = np.where(self.card == draw)
        for i,j in zip(I,J):
            self.cardState[i,j] = 1
    def checkWin(self):
        won = False
        for axis in self.cardState, self.cardState.T:
            for row in axis:
                if all(row):
                    won = True
        return won
    def computeBaseScore(self):
        return self.card[
            np.nonzero(
                self.cardState==0
            )
        ].sum()


class Game:
    def __init__(self, draws, boards):
        self.boards = [Board(b) for b in boards]
        self.draws = draws
    def play(self):
        for draw in self.draws:
            print(f'------------------------- {draw}\n')
            for i,board in enumerate(self.boards):
                board.updateState(draw)
                print(f'{i+1}.\n{board}{board.checkWin()}\n')
                if board.checkWin():
                    print(board, board.computeBaseScore() * draw)
                    return

game = Game(draws, boards)
game.play()
# %%
