class Cell:
    def __init__(self, x, y, moveLeft, moveRight):
        self.x = x
        self.y = y
        self.moveLeft = moveLeft
        self.moveRight = moveRight

    def canMoveLeft(self):
        return self.moveLeft

    def canMoveRight(self):
        return self.moveRight

    def __str__(self):
        return 'x = ' + str(self.x) + ' y = ' + str(self.y) \
               + '\nMove right: ' + str(self.moveRight) + '\nMove left: ' + str(self.moveLeft) + '\n'

    def __repr__(self):
        return self.__str__()