def is_solvable(num):
    counter = 0
    for i in range(0, 9):
        for j in range(1 + i, 9):
            if num[i] > num[j] and num[i] != 0 and num[j] != 0:
                counter += 1
    print(f'inverse num: {counter}')
    if counter % 2 == 0:
        return True
    else:
        return False