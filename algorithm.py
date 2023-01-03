from puzzle import Puzzle


def aStar_manhattan(node, goal):
    start_node = Puzzle(node.get_state(), None, None, 0)
    goal_node = Puzzle(goal.get_state(), None, None, 0)

    open_list = [start_node]
    closed_list = []

    while open_list:
        print("im IN")

        # sort list, so that the node with the lowest total cost is at the top and pop that node
        open_list.sort(key=lambda x: x.total_cost)
        expand_node = open_list.pop(0)
        closed_list.append(expand_node)

        if expand_node.get_state() == goal_node.get_state():
            print("Puzzle solved !!!!")
            exit()

        # expand the top node and add all elements into list only if they ar not None
        if expand_node.move_up() is not None and expand_node.move_up().get_state() not in open_list:
            open_list.append(expand_node.move_up())

        if expand_node.move_down() is not None and expand_node.move_down().get_state() not in open_list :
            open_list.append(expand_node.move_down())

        if expand_node.move_right() is not None and expand_node.move_right().get_state() not in open_list:
            open_list.append(expand_node.move_right())

        if expand_node.move_left() is not None and expand_node.move_left().get_state() not in open_list:
            open_list.append(expand_node.move_left())

        counter = 0
        # for i in open_list:
        #     if open_list[counter] is not None:
        #         print(open_list[counter].get_state())
        #         print("cost: " + str(open_list[counter].cost) + " manhattan cost: " + str(open_list[counter].manhattan_distance()) + " total cost: " + str(open_list[counter].total_cost))
        #     counter += 1
        # if len(closed_list) == 300:
        #     print("closed list elements: " + str(closed_list))
        #     print(len(closed_list))
        #     exit()

        print("----------------------------------------------")
        print("----------------------------------------------")