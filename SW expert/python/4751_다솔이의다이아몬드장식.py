import sys

sys.stdin = open("4751_다솔이의다이아몬드장식.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    str_ = list(input())
    len_ = len(str_) * 4 + 1
    arr = [[0] * len_ for _ in range(5)]

    for i in range(len(str_)):
        for j in range(5):
            if j == 2:
                arr[j][(2 - j % 3)+i*4] = '#'
                arr[j][(2 + j % 3)+i*4] = '#'
                arr[j][2+i*4] = str_[i]
            else:
                arr[j][(2 - j % 2)+i*4] = '#'
                arr[j][(2 + j % 2)+i*4] = '#'

    for i in range(5):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                arr[i][j] = '.'

    for i in arr:
        print(''.join(i))
