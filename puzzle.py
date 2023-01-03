class Puzzle:

    def __init__(self, state, direction, parent, cost):
        self.state = state
        self.direction = direction
        self.parent = parent
        self.cost = cost
        self.total_cost = cost + self.manhattan_distance()

    def get_state(self):
        return self.state

    def find_empty(self):
        x = 0
        for i in self.state:
            if i == 0:
                return x
            x = x + 1

    def swap(self, x, y):
        list = []
        for i in self.state:
            list.append(i)
        list[x] = list[y]
        list[y] = 0
        return list

    def misplaced_tiles(self):
        x = 0
        counter = 0
        for i in self.state:
            if i != x:
                counter = counter + 1
            x = x + 1
        return counter

    def manhattan_distance(self):
        start_index = 0
        counter = 0
        sum = 0
        for i in self.state:
            if i == self.state[counter]:
                goal_index = i
                distance = abs(start_index // 3 - goal_index // 3) + abs(start_index % 3 - goal_index % 3)
                sum = sum + distance
            start_index = start_index +1
            counter = counter + 1
        return sum

    def move_up(self):
        empty = self.find_empty()
        if empty in (0, 1, 2):
            print("cant move up")
            return None
        else:
            new_state = self.swap(empty, empty - 3)
            return Puzzle(new_state, 'move_up', self, self.cost + 1)

    def move_down(self):
        empty = self.find_empty()
        if empty in (6, 7, 8):
            print("cant move down")
            return None
        else:
            new_state = self.swap(empty, empty + 3)
            return Puzzle(new_state, 'move_down', self, self.cost + 1)

    def move_left(self):
        empty = self.find_empty()
        if empty in (0, 3, 6):
            print("cant move left")
            return None
        else:
            new_state = self.swap(empty, empty - 1)
            return Puzzle(new_state, 'move_left', self, self.cost + 1)

    def move_right(self):
        empty = self.find_empty()
        if empty in (2, 5, 8):
            print("cant move right")
            return None
        else:
            new_state = self.swap(empty, empty + 1)
            return Puzzle(new_state, 'move_right', self, self.cost + 1)


