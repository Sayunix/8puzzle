from puzzle import Puzzle
from printfield import print_field

# aStar algorithm with manhattan heuristic
# todo aStar beschreiben und manhattan heuristic

def aStar_manhattan(node, goal):
    open_list = [node]
    hallo = [node.get_state()]
    closed_list = []
    counter = 0

    while open_list:
        # sort list, so that the node with the lowest total cost is at the top and pop that node
        open_list.sort(key=lambda x: x.total_manhattan)
        expand_node = open_list.pop(0)
        closed_list.append(expand_node)

        if expand_node.get_state() == goal.get_state():
            return print("Puzzle solved!")

        # expand the top node and add all elements into list only if they are not None
        if expand_node.direction != "move_down":
            if expand_node.move_up() is not None and expand_node.move_up().get_state() not in hallo:
                newNode = expand_node.move_up()
                # print_field(newNode.get_state())
                hallo.append(newNode.get_state())
                open_list.append(newNode)

        if expand_node.direction != "move_up":
            if expand_node.move_down() is not None and expand_node.move_down().get_state() not in hallo:
                newNode = expand_node.move_down()
                # print_field(newNode.get_state())
                hallo.append(newNode.get_state())
                open_list.append(newNode)

        if expand_node.direction != "move_left":
            if expand_node.move_right() is not None and expand_node.move_right().get_state() not in hallo:
                newNode = expand_node.move_right()
                # print_field(newNode.get_state())
                hallo.append(newNode.get_state())
                open_list.append(newNode)

        if expand_node.direction != "move_right":
            if expand_node.move_left() is not None and expand_node.move_left().get_state() not in hallo:
                newNode = expand_node.move_left()
                # print_field(newNode.get_state())
                hallo.append(newNode.get_state())
                open_list.append(newNode)


        counter += 1
        #print(str(counter) + "----------------------------------------------")
        #print("----------------------------------------------")
    print(counter)

# aStar algorithm with hamming heuristic
#todo aStar beschreiben und hamming heuristic

def aStar_misplaced(node, goal):
    open_list = [node]
    hallo = [node.get_state()]
    closed_list = []
    counter = 0

    while open_list:
        # sort list, so that the node with the lowest total cost is at the top and pop that node
        open_list.sort(key=lambda x: x.total_misplaced)
        expand_node = open_list.pop(0)
        closed_list.append(expand_node)

        if expand_node.get_state() == goal.get_state():
            print("Puzzle solved!")
            print("nodes expanded:" + str(counter))
            return expand_node

        # expand the top node and add all elements into list only if they are not None
        if expand_node.direction != "move_down":
            if expand_node.move_up() is not None and expand_node.move_up().get_state() not in hallo:
                newNode = expand_node.move_up()
                # print_field(newNode.get_state())
                hallo.append(newNode.get_state())
                open_list.append(newNode)

        if expand_node.direction != "move_up":
            if expand_node.move_down() is not None and expand_node.move_down().get_state() not in hallo:
                newNode = expand_node.move_down()
                # print_field(newNode.get_state())
                hallo.append(newNode.get_state())
                open_list.append(newNode)

        if expand_node.direction != "move_left":
            if expand_node.move_right() is not None and expand_node.move_right().get_state() not in hallo:
                newNode = expand_node.move_right()
                # print_field(newNode.get_state())
                hallo.append(newNode.get_state())
                open_list.append(newNode)

        if expand_node.direction != "move_right":
            if expand_node.move_left() is not None and expand_node.move_left().get_state() not in hallo:
                newNode = expand_node.move_left()
                # print_field(newNode.get_state())
                hallo.append(newNode.get_state())
                open_list.append(newNode)

        counter += 1
        #print(str(counter) + "----------------------------------------------")
        #print("----------------------------------------------")