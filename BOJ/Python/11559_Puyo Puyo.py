# baekjoon source = "https://www.acmicpc.net/problem/11559"

'''
......
......
......
......
......
....Y.
....Y.
....Y.
....RR
...YRR
..GGYY
..GGYY

......
......
......
......
......
......
....Y.
....Y.
....RR
...YRR
..GGYY
..GGYY

RRRRRR
RRRRRR
RRRRRR
RRRRRR
RRRRRR
RRBBRR
RRRRRR
RRRRRR
RRRRRR
RRBBRR
RRRRRR
RRRRRR

......
......
......
......
......
......
......
......
......
......
......
......
'''
import sys
from collections import deque

def check(x, y, z):
    if x < 0 or x > n - 1: return False
    if y < 0 or y > 5: return False
    if visited[x][y]: return False
    if z != arr[x][y]: return False
    return True

def solution(x, y):
    q = deque([[x, y]])
    visited[x][y] = 1
    count = 1
    index = 0
    len_ = 1
    while index < len_:
        t = q[index]
        for i in range(4):
            tx = t[0] + dx[i]
            ty = t[1] + dy[i]
            if check(tx, ty, arr[x][y]):
                q.append([tx, ty])
                visited[tx][ty] = 1
                count += 1
                len_ += 1
        index += 1

    if count >= 4:
        change(q)
        return q

    return False

def change(x):
    num = [0] * 6
    cnt = [0] * 6
    for i in x:
        arr[i[0]][i[1]] = '.'
        num[i[1]] = max(num[i[1]], i[0])
        cnt[i[1]] += 1

    for i in range(6):
        if num[i] == 0:
            continue

        index = num[i]
        for j in range(num[i], -1, -1):
            if arr[j][i] != '.':
                arr[j][i], arr[index][i] = arr[index][i], arr[j][i]
                index -= 1

arr = []
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
n = 0
flag = True
for i in range(12):
    input_ = list(sys.stdin.readline().strip())
    if flag:
        for j in range(6):
            if input_[j] != '.':
                break
        else:
            continue
        flag = False
        arr.append(input_)
        n += 1
    else:
        arr.append(input_)
        n += 1

result = 0
flag = False
visited = [[0] * 6 for _ in range(n)]
r = False
for i in range(n):
    for j in range(6):
        if arr[i][j] != '.' and not visited[i][j]:
            r = solution(i, j)
            if r:
                flag = True
                result += 1
                break
    if flag:
        break

while r:
    visited = [[0] * 6 for _ in range(n)]
    for i in r:
        if arr[i[0]][i[1]] != '.':
            a = solution(i[0], i[1])
            if a:
                result += 1
                r = a
                break
    else:
        break

print(result)
