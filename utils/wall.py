class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.id = 0

    def equal(self, x, y):
        return self.x == x and self.y == y