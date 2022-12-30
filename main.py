from printfield import print_field
from printfield import gen_num
from solvability import is_solvable
from node import Node

num = gen_num()
goalstate = [0, 1, 2, 3, 4, 5, 6, 7, 8]
randomfield = num
node = Node(num)


def main():
    print("Goalstate: ")
    print_field(goalstate)
    print("random field: ")
    print_field(randomfield)

    if not is_solvable(randomfield):
        print("is not solvable")
        exit()

    while True:
        i = input("left(l), right(r), up(u), down(d): ")
        if i == "l":
            print_field(node.move_left())
        elif i == "r":
            print_field(node.move_right())
        elif i == "u":
            print_field(node.move_up())
        elif i == "d":
            print_field(node.move_down())
        elif i == "e":
            exit()
        else:
            print("pls enter a valid command")

        if goalstate == randomfield:
            print("puzzle solved")
            exit()


if __name__ == '__main__':
    main()
