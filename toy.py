class Toy:
    def __init__(self, bonus = 10, newness = 10):
        self.bonus = bonus
        self.newness = newness

    def use(self):
        if (self.newness > 0):
            self.newness -= 1
            return self.bonus
        else:
            return 


