class Node:

    def __init__(self, state):
        self.state = state

    def find_zero(self):
        x = 0
        for i in self.state:
            if i == 0:
                return x
            x = x + 1

    def swap(self, x, y):
        self.state[x] = self.state[y]
        self.state[y] = 0

    def move_up(self):
        zero = self.find_zero()
        if zero in (0, 1, 2):
            print("cant move up")
            return self.state
        else:
            self.swap(zero, zero - 3)
            return self.state

    def move_down(self):
        zero = self.find_zero()
        if zero in (6, 7, 8):
            print("cant move down")
            return self.state
        else:
            self.swap(zero, zero + 3)
            return self.state

    def move_left(self):
        zero = self.find_zero()
        if zero in (0, 3, 6):
            print("cant move left")
            return self.state
        else:
            self.swap(zero, zero - 1)
            return self.state

    def move_right(self):
        zero = self.find_zero()
        if zero in (2, 5, 8):
            print("cant move right")
            return self.state
        else:
            self.swap(zero, zero + 1)
            return self.state


