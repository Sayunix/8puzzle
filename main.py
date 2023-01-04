from printfield import print_field
from printfield import gen_num
from solvability import is_solvable
from puzzle import Puzzle
from algorithm import aStar_manhattan
from algorithm import aStar_misplaced
import time

# Defines the goal-state of the puzzle in a List
goalstate = [0, 1, 2, 3, 4, 5, 6, 7, 8]
goalstate_node = Puzzle(goalstate, None, None, 0)
# randomfield = [1, 2, 0, 3, 4, 5, 6, 7, 8]



# Prints the goal state and a random state of a field, checks if the random field is solvable
# Prints the current results of the two heuristics
# Asks for User input to choose manhattan or hamming heuristic to solve puzzle
# Solves puzzle based on given user input with chosen heuristic, or exists program on invalid input
def main():
    randomfield = gen_num()
    start_node = Puzzle(randomfield, None, None, 0)

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
    aStar_manhattan(start_node, goalstate_node)

    #aStar_misplaced(start_node, goalstate_node)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
