class Puzzle:
    # Constructor for puzzle object
    def __init__(self, state, direction, parent, cost):
        self.state = state
        self.direction = direction
        self.parent = parent
        self.cost = cost
        self.total_manhattan = cost + self.manhattan_distance()
        self.total_misplaced = cost + self.misplaced_tiles()

    # Gets current state of puzzle
    def get_state(self):
        return self.state

    # Finds position of empty field
    def find_empty(self):
        x = 0
        for i in self.state:
            if i == 0:
                return x
            x = x + 1

    # Swaps number and zero in field
    def swap(self, x, y):
        list = []
        for i in self.state:
            list.append(i)
        list[x] = list[y]
        list[y] = 0
        return list

    # Returns misplaced tiles
    def misplaced_tiles(self):
        x = 0
        counter = 0
        for i in self.state:
            if i != x:
                counter = counter + 1
            x = x + 1
        return counter

    # Returns sum of field distance between current state and goal state
    def manhattan_distance(self):
        start_index = 0
        counter = 0
        sum = 0
        for i in self.state:
            if i == self.state[counter]:
                goal_index = i
                distance = abs(start_index // 3 - goal_index // 3) + abs(start_index % 3 - goal_index % 3)
                sum = sum + distance
            start_index = start_index + 1
            counter = counter + 1
        return sum

    # Moves empty field up or returns None if not possible
    def move_up(self):
        empty = self.find_empty()
        if empty in (0, 1, 2):
            return None
        else:
            new_state = self.swap(empty, empty - 3)
            return Puzzle(new_state, 'move_up', self, self.cost + 1)

    # Moves empty field down or returns None if not possible
    def move_down(self):
        empty = self.find_empty()
        if empty in (6, 7, 8):
            return None
        else:
            new_state = self.swap(empty, empty + 3)
            return Puzzle(new_state, 'move_down', self, self.cost + 1)

    # Moves empty field left or returns None if not possible
    def move_left(self):
        empty = self.find_empty()
        if empty in (0, 3, 6):
            return None
        else:
            new_state = self.swap(empty, empty - 1)
            return Puzzle(new_state, 'move_left', self, self.cost + 1)

    # Moves empty field right or returns None if not possible
    def move_right(self):
        empty = self.find_empty()
        if empty in (2, 5, 8):
            return None
        else:
            new_state = self.swap(empty, empty + 1)
            return Puzzle(new_state, 'move_right', self, self.cost + 1)
