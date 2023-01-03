import random


def gen_num():
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(num)
    return num


def print_field(rfield):

    field = [[rfield[0], rfield[1], rfield[2]], [rfield[3], rfield[4], rfield[5]], [rfield[6], rfield[7], rfield[8]]]
    print("_____________")
    for k in field:
        print("|", end="")
        for j in k:
            if j == 0:
                j = " "
            print(f' {j} |', end="")
        print()
        print("-------------")
