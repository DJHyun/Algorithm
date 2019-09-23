# baekjoon source = "https://www.acmicpc.net/problem/16234"
import sys
from collections import deque

def check(x, y):
    if x < 0 or x > N - 1: return False
    if y < 0 or y > N - 1: return False
    if visited[x][y] >= index: return False
    return True

def solution(x, y, flag):
    q = deque([[x, y]])
    visited[x][y] = index
    sum_ = arr[x][y]
    cnt = 1
    q_index = 0

    while q_index < len(q):
        t = q[q_index]
        for i in range(4):
            tx = t[0] + dx[i]
            ty = t[1] + dy[i]
            if check(tx, ty) and L <= abs(arr[t[0]][t[1]] - arr[tx][ty]) <= R:
                sum_ += arr[tx][ty]
                visited[tx][ty] = index
                cnt += 1
                flag = False
                q.append([tx, ty])

        q_index += 1

    for i in range(q_index):
        arr[q[i][0]][q[i][1]] = sum_ // cnt

    return flag

N, L, R = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
index = 1
result = 0

while_flag = True
while while_flag:
    flag = True

    for i in range(N):
        for j in range(N):
            if visited[i][j] < index:
                flag = solution(i, j, flag)

    if flag:
        while_flag = False
        break
    else:
        result += 1

    index += 1
print(result)
