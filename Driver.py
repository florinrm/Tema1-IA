import copy
import moves
from Cell import Cell

class Driver:
    def __init__(self, x, y, fuel, table):
        self.x = x
        self.y = y
        self.fuel = fuel
        self.table = table
        self.destinationX = 0
        self.destinationY = 0
        self.depth = 0
        self.parent = None
        self.costFromInitial = 0
        self.estimatedCost = 0
        self.lastMove = None

    def moveDriver(self, move):
        if self.fuel > 0:
            if move == moves.DOWN:
                if self.canGoDown():
                    self.y = self.y + 1
                    self.fuel = self.fuel - 1
                    self.depth = self.depth + 1
                    self.lastMove = moves.DOWN
                else:
                    print('CANNOT MOVE DOWN - BORDER REACHED')
            elif move == moves.UP:
                if self.canGoUp():
                    self.y = self.y - 1
                    self.fuel = self.fuel - 1
                    self.depth = self.depth + 1
                    self.lastMove = moves.UP
                else:
                    print('CANNOT MOVE UP - BORDER REACHED')
            elif move == moves.RIGHT:
                if self.canGoRight():
                    self.x = self.x + 1
                    self.fuel = self.fuel - 1
                    self.depth = self.depth + 1
                    self.lastMove = moves.RIGHT
                else:
                    print('CANNOT MOVE RIGHT - BORDER REACHED')
            elif move == moves.LEFT:
                if self.canGoLeft():
                    self.x = self.x - 1
                    self.fuel = self.fuel - 1
                    self.depth = self.depth + 1
                    self.lastMove = moves.LEFT
                else:
                    print('CANNOT MOVE LEFT - BORDER REACHED')
        else:
            print('RUN OUT OF FUEL')

    def canGoRight(self):
        return self.fuel > 0 and self.x + 1 < len(self.table[0]) and self.table[self.x][self.y].canMoveRight()

    def canGoLeft(self):
        return self.fuel > 0 and self.x > 0 and self.table[self.x][self.y].canMoveLeft()

    def canGoUp(self):
        return self.fuel > 0 and self.y > 0

    def canGoDown(self):
        return self.fuel > 0 and self.y + 1 < len(self.table)

    def succesors(self):
        succ = []
        if self.canGoDown():
            next1 = copy.deepcopy(self)
            next1.moveDriver(moves.DOWN)
            succ.append(next1)

        if self.canGoUp():
            next2 = copy.deepcopy(self)
            next2.moveDriver(moves.UP)
            succ.append(next2)

        if self.canGoRight():
            next3 = copy.deepcopy(self)
            next3.moveDriver(moves.RIGHT)
            succ.append(next3)

        if self.canGoLeft():
            next4 = copy.deepcopy(self)
            next4.moveDriver(moves.LEFT)
            succ.append(next4)

        return succ

    def __str__(self):
        return 'Current position: ' + str(self.x) + ' ' + str(self.y) \
               + '\n' + 'Destination: ' + str(self.destinationX) + ' ' + str(self.destinationY) \
               + '\nCurrent fuel: ' + str(self.fuel) + '\n' \
               #+ str(self.table)

    def __repr__(self):
        return self.__str__()

    def goal(self):
        return self.fuel >= 0 and (self.x == self.destinationX) and (self.y == self.destinationY)

    def copy(self):
        return self