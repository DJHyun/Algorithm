import sys

sys.stdin = open("5356_의석이의세로로말해요.txt","r")

T = int(input())
for test_case in range(1, T + 1):
    arr = [list(input()) for _ in range(5)]

    max_ = 0
    for i in range(len(arr)):
        max_ = max(max_,len(arr[i]))

    for i in range(len(arr)):
        if len(arr[i]) != max_:
            for j in range(max_-len(arr[i])):
                arr[i].append('')

    print('#{} '.format(test_case),end='')
    for i in range(len(arr[0])):
        for j in range(len(arr)):
            print(arr[j][i],end='')
    print()
