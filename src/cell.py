class Cell:
    def __init__(self, direc, dist, body):
        self.e_type = body.e_type
        self.direc = direc
        self.dist = dist
        self.body = body

    def get_type(self):
        return self.e_type

    def get_pos(self, cent):
        return cent + self.direc * self.dist

    def turn(self, direc):
        self.direc += direc
        self.body.turn(direc)

    def give_power(self):
        return self.body.give_power()