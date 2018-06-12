class MoneyBox:
    def __init__(self, capacity):
        self.v = 0
        self.capacity = capacity

    def can_add(self, v):
        return self.v + v <= self.capacity

    def add(self, v):
        self.v += v