from printfield import print_field
from printfield import gen_num
from solvability import is_solvable
from puzzle import Puzzle
from algorithm import aStar_manhattan
from algorithm import aStar_misplaced
import time


# Prints the goal state and a random state of a field, checks if the random field is solvable
# Prints the current results of the two heuristics
# Asks for User input to choose manhattan or hamming heuristic to solve puzzle
# Solves puzzle based on given user input with chosen heuristic, or exists program on invalid input
def main1():
    counter_manhattan = 0
    i = 0
    while i <= 100:
        randomfield = gen_num()
        start_node = Puzzle(randomfield, None, None, 0)

        # print("Goalstate: ")
        # print_field(goalstate)
        # print("Random field: ")
        # print_field(randomfield)

        if not is_solvable(randomfield):
            i+=1
            print("is not solvable")
            continue
        expanded_nodes = aStar_manhattan(start_node, goalstate_node)
        counter_manhattan += expanded_nodes
        i+=1
    return counter_manhattan


def main2():
    counter_hemming = 0
    i = 0
    while i <= 100:
        randomfield = gen_num()
        start_node = Puzzle(randomfield, None, None, 0)

        if not is_solvable(randomfield):
            print("is not solvable")
            continue
        expanded_nodes = aStar_misplaced(start_node, goalstate_node)
        counter_hemming += expanded_nodes
        i+=1
    return counter_hemming


if __name__ == '__main__':
    # Defines the goal-state of the puzzle in a List
    goalstate = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    goalstate_node = Puzzle(goalstate, None, None, 0)
    # randomfield = [1, 2, 0, 3, 4, 5, 6, 7, 8]
    start_main1 = time.time()
    counter1 = main1()
    total_time1 = time.time() - start_main1
    print("manhattan finished")
    #start_main2 = time.time()
    #counter2 = main2()
    #total_time2 = time.time() - start_main2
    print("Manhattan:")
    print("Average nodes expanded: " + str(counter1 / 100))
    print("--- %s seconds --- in total" % total_time1)
    print(" %s seconds on average" % (total_time1 / 100))

    #print("Hemming:")
    #print("Average nodes expanded: " + str(counter2 / 100))
    #print("--- %s seconds --- in total" % total_time2)
    #print(" %s seconds on average" % (total_time2 / 100))
