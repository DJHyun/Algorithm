# baekjoon source = "https://www.acmicpc.net/problem/15685"
'''
3
3 3 0 1
4 2 1 3
4 2 2 1
'''
import sys

def direction(x, y, d):
    if d == 0:
        y += 1
    elif d == 1:
        x -= 1
    elif d == 2:
        y -= 1
    else:
        x += 1

    return x, y

def turn(d):
    if d == 0:
        d = 1
    elif d == 1:
        d = 2
    elif d == 2:
        d = 3
    else:
        d = 0

    return d

N = int(sys.stdin.readline())
arr = [[0] * 101 for _ in range(101)]
cnt = 0

for i in range(N):
    y, x, d, g = map(int, sys.stdin.readline().split())
    arr[x][y] = 1
    result = [[x, y]]
    dire = [d]

    for i in range(g + 1):
        len_ = len(dire)
        for j in range(len_ - 1, -1, -1):
            if i == 0:
                x, y = direction(result[j][0], result[j][1], dire[j])
                result[0] = (x, y)
                arr[x][y] = 1
            else:
                d = turn(dire[j])
                dire.append(d)
                x, y = direction(result[0][0], result[0][1], d)
                result[0] = (x, y)
                arr[x][y] = 1

for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i][j + 1]:
            if arr[i+1][j + 1] and arr[i + 1][j]:
                cnt += 1

print(cnt)
