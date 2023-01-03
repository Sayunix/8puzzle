from printfield import print_field
from printfield import gen_num
from solvability import is_solvable
from puzzle import Puzzle
from algorithm import aStar_manhattan

num = gen_num()
goalstate = [0, 1, 2, 3, 4, 5, 6, 7, 8]
randomfield = num
# randomfield = [1, 0, 2, 3, 4, 5, 6, 7, 8]
start_node = Puzzle(randomfield, None, None, 0)
goalstate_node = Puzzle(goalstate, None, None, 0)


def main():
    print("Goalstate: ")
    print_field(goalstate)
    print("random field: ")
    print_field(randomfield)

    if not is_solvable(randomfield):
        print("is not solvable")
        exit()

    aStar_manhattan(start_node, goalstate_node)
    print("number of misplaced tiles: " + str(start_node.misplaced_tiles()))
    print("Manhattan distance: " + str(start_node.manhattan_distance()))
    print("total cost of this board: " + str(start_node.total_cost))

    if goalstate == randomfield:
        print("puzzle solved")
        exit()


if __name__ == '__main__':
    main()


