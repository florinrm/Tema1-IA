import moves
import Cell

class Driver:
    def __init__(self, x, y, fuel, table):
        self.x = x
        self.y = y
        self.fuel = fuel
        self.table = table
        self.destinationX = 0
        self.destinationY = 0

    def moveDriver(self, move):
        if move == moves.DOWN:
            if (self.y + 1) < len(self.table):
                self.y = self.y + 1
        elif move == moves.UP:
            if (self.y - 1) >= 0:
                self.y = self.y - 1
        elif move == moves.RIGHT:
            if self.table[self.x][self.y].canMoveRight():
                self.x = self.x + 1
        elif move == moves.LEFT:
            if self.table[self.x][self.y].canMoveLeft():
                self.x = self.x - 1