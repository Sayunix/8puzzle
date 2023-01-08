from puzzle import Puzzle
from printfield import print_field


# A* is a searching algorithm that is used to find the shortest path between an initial and a final point.
# It searches for shorter paths first, thus making it an optimal and complete algorithm.
# An optimal algorithm will find the least cost outcome for a problem,
# while a complete algorithm finds all the possible outcomes of a problem.
# https://www.simplilearn.com/tutorials/artificial-intelligence-tutorial/a-star-algorithm

# Manhattan heuristic: The sum of the misplaced tiles if the generated field is compared to the goal field

# aStar algorithm with manhattan heuristic
def aStar_manhattan(node, goal):
    open_list = [node]
    open_state = [node.get_state()]
    closed_list = []
    counter = 0

    while open_list:
        # sort list, so that the node with the lowest total cost is at the top and pop that node
        open_list.sort(key=lambda x: x.total_manhattan)
        expand_node = open_list.pop(0)
        closed_list.append(expand_node.get_state)
        counter += 1

        if expand_node.get_state() == goal.get_state():
            print("Puzzle solved!")
            return counter

        # expand the top node and add all elements into list only if they are not None
        nodeUp = expand_node.move_up()
        nodeDown = expand_node.move_down()
        nodeRight = expand_node.move_right()
        nodeLeft = expand_node.move_left()
        if expand_node.direction != "move_down":
            if nodeUp is not None:
                if nodeUp.get_state() not in open_state and nodeUp.get_state() not in closed_list:
                    open_state.append(nodeUp.get_state())
                    open_list.append(nodeUp)

        if expand_node.direction != "move_up":
            if nodeDown is not None:
                if nodeDown.get_state() not in open_state or nodeDown.get_state() not in closed_list:
                    open_state.append(nodeDown.get_state())
                    open_list.append(nodeDown)

        if expand_node.direction != "move_left":
            if nodeRight is not None:
                if nodeRight.get_state() not in open_state and nodeRight.get_state() not in closed_list:
                    open_state.append(nodeRight.get_state())
                    open_list.append(nodeRight)

        if expand_node.direction != "move_right":
            if nodeLeft is not None:
                if nodeLeft.get_state() not in open_state and nodeLeft.get_state() not in closed_list:
                    open_state.append(nodeLeft.get_state())
                    open_list.append(nodeLeft)

# aStar algorithm with hamming heuristic
# Hamming heuristic: Hamming distance is the total number of misplaced tiles.

def aStar_misplaced(node, goal):
    open_list = [node]
    open_state = [node.get_state()]
    closed_list = []
    counter = 0

    while open_list:
        # sort list, so that the node with the lowest total cost is at the top and pop that node
        open_list.sort(key=lambda x: x.total_misplaced)
        expand_node = open_list.pop(0)
        closed_list.append(expand_node)
        counter += 1

        if expand_node.get_state() == goal.get_state():
            print("Puzzle solved!")
            return counter

        # expand the top node and add all elements into list only if they are not None
        nodeUp = expand_node.move_up()
        nodeDown = expand_node.move_down()
        nodeRight = expand_node.move_right()
        nodeLeft = expand_node.move_left()
        if expand_node.direction != "move_down":
            if nodeUp is not None:
                if nodeUp.get_state() not in open_state and nodeUp.get_state() not in closed_list:
                    open_state.append(nodeUp.get_state())
                    open_list.append(nodeUp)

        if expand_node.direction != "move_up":
            if nodeDown is not None:
                if nodeDown.get_state() not in open_state or nodeDown.get_state() not in closed_list:
                    open_state.append(nodeDown.get_state())
                    open_list.append(nodeDown)

        if expand_node.direction != "move_left":
            if nodeRight is not None:
                if nodeRight.get_state() not in open_state and nodeRight.get_state() not in closed_list:
                    open_state.append(nodeRight.get_state())
                    open_list.append(nodeRight)

        if expand_node.direction != "move_right":
            if nodeLeft is not None:
                if nodeLeft.get_state() not in open_state and nodeLeft.get_state() not in closed_list:
                    open_state.append(nodeLeft.get_state())
                    open_list.append(nodeLeft)


