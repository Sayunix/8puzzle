from printfield import print_field
from printfield import gen_num
from solvability import is_solvable
from puzzle import Puzzle
from algorithm import aStar_manhattan
from algorithm import aStar_misplaced
import time

num = gen_num()
# Defines the goal-state of the puzzle in a List
goalstate = [0, 1, 2, 3, 4, 5, 6, 7, 8]
randomfield = num
# randomfield = [1, 2, 0, 3, 4, 5, 6, 7, 8]
start_node = Puzzle(randomfield, None, None, 0)
goalstate_node = Puzzle(goalstate, None, None, 0)


def main():
    print("Goalstate: ")
    print_field(goalstate)
    print("Random field: ")
    print_field(randomfield)

    if not is_solvable(randomfield):
        print("is not solvable")
        exit()

    print("number of misplaced tiles: " + str(start_node.misplaced_tiles()))
    print("Manhattan distance: " + str(start_node.manhattan_distance()))

    print("----------------------------------------------")
    man_or_mis = input("Solve puzzle with manhattan <man> or number of misplaced <mis> tiles: ")
    if man_or_mis == "man":
        start = time.time()
        aStar_manhattan(start_node, goalstate_node)
        print((time.time() - start))
    elif man_or_mis == "mis":
        start = time.time()
        aStar_misplaced(start_node, goalstate_node)
        print((time.time() - start))
    else:
        print("please give a valid answer")


if __name__ == '__main__':
    main()
