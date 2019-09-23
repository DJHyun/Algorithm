import sys

sys.stdin = open('input.txt', 'r')

def check(x, y, v):
    if arr[x][y] != -1:
        if arr[x][y][1] == 0 and arr[x][y][2] == 0:
            if arr[x][y][0] > v:
                return False
        else:
            return False
    if arr[x][y] == -1: return False
    return True

def solution(x, y, v):
    global cnt
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if check(tx, ty, v):
            arr[tx][ty] = [v, 0, 0]
            cnt += 1

test_case = int(input())
for t in range(1, 2):
    n, m, k = map(int, input().split())
    arr = [[[0, 0, 0] for i in range(20)] for j in range(20)]
    result = 0
    cnt = 0
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

    for i in range(n):
        numbers = list(map(int, input().split()))
        for j in range(m):
            if numbers[j] != 0:
                cnt += 1
            arr[i + 4][j + 4][0] = numbers[j]
    for i in arr:
        print(i)
    print()
    while result < k:
        result += 1
        for i in range(10):
            for j in range(10):
                if arr[i][j] != -1 and arr[i][j][0] != 0  :
                    if arr[i][j][1] != 1:
                        arr[i][j][2] += 1
                        if arr[i][j][2] == arr[i][j][0]:
                            arr[i][j][2] = 0
                            arr[i][j][1] = 1
                    else:
                        arr[i][j][2] += 1
                        if arr[i][j][1] == 1 and arr[i][j][2] == arr[i][j][0]:
                            solution(i, j, arr[i][j][0])
                            arr[i][j] = -1
                            cnt -= 1

        for i in arr:
            print(i)
        print()

    print(cnt)
