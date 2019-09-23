# baekjoon source = "https://www.acmicpc.net/problem/14499"
import sys



def solution(b):
    if b == 1:
        ju[1][0], ju[1][1], ju[1][2], ju[3][1] = ju[1][1], ju[1][2], ju[3][1], ju[1][0]
    elif b == 2:
        ju[1][0], ju[1][1], ju[1][2], ju[3][1] = ju[3][1], ju[1][0], ju[1][1], ju[1][2]
    elif b == 3:
        ju[0][1], ju[1][1], ju[2][1], ju[3][1] = ju[3][1], ju[0][1], ju[1][1], ju[2][1]
    else:
        ju[0][1], ju[1][1], ju[2][1], ju[3][1] = ju[1][1], ju[2][1], ju[3][1], ju[0][1]

def check(x, y):
    if x < 0 or x > n - 1: return False
    if y < 0 or y > m - 1: return False
    return True

n, m, x, y, k = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
command = list(map(int, sys.stdin.readline().split()))
ju = [[0] * 3 for _ in range(4)]

for i in range(k):
    if command[i] == 1:
        y += 1
        if check(x, y):
            solution(command[i])
            if arr[x][y] == 0:
                arr[x][y] = ju[1][1]
            else:
                ju[1][1], arr[x][y] = arr[x][y], 0
            print(ju[3][1])
        else:
            y -= 1
    elif command[i] == 2:
        y -= 1
        if check(x, y):
            solution(command[i])
            if arr[x][y] == 0:
                arr[x][y] = ju[1][1]
            else:
                ju[1][1], arr[x][y] = arr[x][y], 0
            print(ju[3][1])
        else:
            y += 1
    elif command[i] == 3:
        x -= 1
        if check(x, y):
            solution(command[i])
            if arr[x][y] == 0:
                arr[x][y] = ju[1][1]
            else:
                ju[1][1], arr[x][y] = arr[x][y], 0
            print(ju[3][1])
        else:
            x += 1
    else:
        x += 1
        if check(x, y):
            solution(command[i])
            if arr[x][y] == 0:
                arr[x][y] = ju[1][1]
            else:
                ju[1][1], arr[x][y] = arr[x][y], 0
            print(ju[3][1])
        else:
            x -= 1

