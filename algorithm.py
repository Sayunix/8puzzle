from puzzle import Puzzle
from printfield import print_field

# aStar algorithm with manhattan heuristic
# todo aStar beschreiben und manhattan heuristic

def aStar_manhattan(node, goal):
    start_node = Puzzle(node.get_state(), None, None, 0)
    goal_node = Puzzle(goal.get_state(), None, None, 0)

    open_list = [start_node]
    closed_list = []
    counter = 0

    while open_list:
        # sort list, so that the node with the lowest total cost is at the top and pop that node
        open_list.sort(key=lambda x: x.total_manhattan)
        expand_node = open_list.pop(0)
        closed_list.append(expand_node)

        if expand_node.get_state() == goal_node.get_state():
            return print("Puzzle solved!")

        # expand the top node and add all elements into list only if they are not None
        if expand_node.direction != "move_down":
            if expand_node.move_up() is not None:
                newNode = expand_node.move_up()
                open_list.append(newNode)
                #print_field(newNode.get_state())
                #print(str(newNode.total_manhattan))

        if expand_node.direction != "move_up":
            if expand_node.move_down() is not None:
                newNode = expand_node.move_down()
                open_list.append(newNode)
                #print_field(newNode.get_state())
                #print(str(newNode.total_manhattan))

        if expand_node.direction != "move_left":
            if expand_node.move_right() is not None:
                newNode = expand_node.move_right()
                open_list.append(newNode)
                #print_field(newNode.get_state())
                #print(str(newNode.total_manhattan))

        if expand_node.direction != "move_right":
            if expand_node.move_left() is not None:
                newNode = expand_node.move_left()
                open_list.append(newNode)
                #print_field(newNode.get_state())
                #print(str(newNode.total_manhattan))


        counter += 1
        #print(str(counter) + "----------------------------------------------")
        #print("----------------------------------------------")
    print(counter)

# aStar algorithm with hamming heuristic
#todo aStar beschreiben und hamming heuristic

def aStar_misplaced(node, goal):
    start_node = Puzzle(node.get_state(), None, None, 0)
    goal_node = Puzzle(goal.get_state(), None, None, 0)

    open_list = [start_node]
    closed_list = []
    counter = 0

    while open_list:
        # sort list, so that the node with the lowest total cost is at the top and pop that node
        open_list.sort(key=lambda x: x.total_misplaced)
        expand_node = open_list.pop(0)
        closed_list.append(expand_node)

        if expand_node.get_state() == goal_node.get_state():
            return print("Puzzle solved!")

        # expand the top node and add all elements into list only if they are not None
        if expand_node.direction != "move_down":
            if expand_node.move_up() is not None:
                newNode = expand_node.move_up()
                open_list.append(newNode)
                print_field(newNode.get_state())
                print(str(newNode.total_misplaced))

        if expand_node.direction != "move_up":
            if expand_node.move_down() is not None:
                newNode = expand_node.move_down()
                open_list.append(newNode)
                print_field(newNode.get_state())
                print(str(newNode.total_misplaced))

        if expand_node.direction != "move_left":
            if expand_node.move_right() is not None:
                newNode = expand_node.move_right()
                open_list.append(newNode)
                print_field(newNode.get_state())
                print(str(newNode.total_misplaced))

        if expand_node.direction != "move_right":
            if expand_node.move_left() is not None:
                newNode = expand_node.move_left()
                open_list.append(newNode)
                print_field(newNode.get_state())
                print(str(newNode.total_misplaced))

        counter += 1
        #print(str(counter) + "----------------------------------------------")
        #print("----------------------------------------------")
    print(counter)