import sys

'''
[8, 8, 4, 4, 0]
[0, 4, 0, 0, 8]
[8, 0, 4, 4, 4]
[2, 4, 0, 2, 8]
[0, 0, 2, 0, 0]
'''
sys.stdin = open("6109_추억의2048게임.txt", "r")


def up():
    for i in range(N):
        for j in range(N):
            if arr[j][i] != 0:
                for a in range(j + 1, N):
                    if arr[a][i] == 0:
                        continue
                    elif arr[j][i] == arr[a][i]:
                        arr[j][i], arr[a][i] = arr[j][i] + arr[a][i], 0
                        break
                    else:
                        break

        for j in range(N):
            if arr[j][i] == 0:
                for a in range(j + 1, N):
                    if arr[a][i] != 0:
                        arr[j][i], arr[a][i] = arr[a][i], 0
                        break


def down():
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            if arr[j][i] != 0:
                for a in range(j - 1, -1, -1):
                    if arr[a][i] == 0:
                        continue
                    elif arr[j][i] == arr[a][i]:
                        arr[j][i], arr[a][i] = arr[j][i] + arr[a][i], 0
                        break
                    else:
                        break

        for j in range(N - 1, -1, -1):
            if arr[j][i] == 0:
                for a in range(j - 1, -1, -1):
                    if arr[a][i] != 0:
                        arr[j][i], arr[a][i] = arr[a][i], 0
                        break


def right():
    for i in range(N):
        for j in range(N - 1, -1, -1):
            if arr[i][j] != 0:
                for a in range(j - 1, -1, -1):
                    if arr[i][a] == 0:
                        continue
                    elif arr[i][j] == arr[i][a]:
                        arr[i][j], arr[i][a] = arr[i][j] + arr[i][a], 0
                        break
                    else:
                        break

        for j in range(N - 1, -1, -1):
            if arr[i][j] == 0:
                for a in range(j - 1, -1, -1):
                    if arr[i][a] != 0:
                        arr[i][j], arr[i][a] = arr[i][a], 0
                        break


def left():
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                for a in range(j + 1, N):
                    if arr[i][a] == 0:
                        continue
                    elif arr[i][j] == arr[i][a]:
                        arr[i][j], arr[i][a] = arr[i][j] + arr[i][a], 0
                        break
                    else:
                        break

        for j in range(N):
            if arr[i][j] == 0:
                for a in range(j + 1, N):
                    if arr[i][a] != 0:
                        arr[i][j], arr[i][a] = arr[i][a], 0
                        break


T = int(input())
for test_case in range(1, T + 1):
    N, S = input().split()
    N = int(N)
    arr = [list(map(int, input().split())) for _ in range(N)]

    if S == 'up':
        up()
    elif S == 'down':
        down()
    elif S == 'right':
        right()
    else:
        left()

    print('#{}'.format(test_case))
    for i in arr:
        print(' '.join(list(map(str, i))))
