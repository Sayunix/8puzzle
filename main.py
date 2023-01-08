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
def main1(rf):
    counter_manhattan = 0
    start_node = Puzzle(rf, None, 0)
    expanded_nodes = aStar_manhattan(start_node, goalstate_node)
    counter_manhattan += expanded_nodes
    return counter_manhattan


def main2(rf):
    counter_hamming = 0
    start_node = Puzzle(rf, None, 0)
    expanded_nodes = aStar_misplaced(start_node, goalstate_node)
    counter_hamming += expanded_nodes
    return counter_hamming


if __name__ == '__main__':
    # Defines the goal-state of the puzzle in a List
    goalstate = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    goalstate_node = Puzzle(goalstate, None, 0)
    randomList = []

    i = 0
    while i < 100:
        randomField = gen_num()
        if not is_solvable(randomField):
            print("is not solvable")
            continue
        randomList.append(randomField)
        i += 1

    index1 = 0
    manhattan_total = 0
    start_main1 = time.time()
    for i in randomList:
        manhattan_total += main1(randomList[index1])
        index1 += 1
    total_time1 = time.time() - start_main1
    print("Manhattan:")
    print("Average nodes expanded: " + str(manhattan_total / 100))
    print("--- %s seconds --- in total" % total_time1)
    print(" %s seconds on average" % (total_time1 / 100))

    index2 = 0
    hamming_total = 0
    start_main2 = time.time()
    for i in randomList:
        hamming_total += main2(randomList[index2])
        index2 += 1
    total_time2 = time.time() - start_main2
    print("Hamming:")
    print("Average nodes expanded: " + str(hamming_total / 100))
    print("--- %s seconds --- in total" % total_time2)
    print(" %s seconds on average" % (total_time2 / 100))






