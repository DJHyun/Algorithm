# baekjoon source = "https://www.acmicpc.net/problem/1600"
import sys
from collections import deque

def check(x, y, z):
    if x < 0 or x > h - 1: return False
    if y < 0 or y > w - 1: return False
    if arr[x][y]: return False
    if visited[x][y][z]: return False
    return True

def solution(x, y):
    q = deque([[x, y, 0]])
    count = 0
    while q:
        len_ = len(q)
        for qq in range(len_):
            t = q.popleft()
            for i in range(12):
                if t[2] >= k:
                    if i > 3:
                        break
                tx = t[0] + dx[i]
                ty = t[1] + dy[i]
                if tx == h - 1 and ty == w - 1:
                    return count + 1
                if i > 3:
                    if check(tx, ty, t[2] + 1):
                        visited[tx][ty][t[2] + 1] = 1
                        q.append([tx, ty, t[2] + 1])
                else:
                    if check(tx, ty, t[2]):
                        visited[tx][ty][t[2]] = 1
                        q.append([tx, ty, t[2]])

        count += 1

    return -1

k = int(sys.stdin.readline())
w, h = map(int, sys.stdin.readline().split())
if w == 1 and h == 1:
    print(0)
else:
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    dx, dy = [0, 0, 1, -1, 1, -1, 2, 2, 1, -1, -2, -2], [1, -1, 0, 0, 2, 2, 1, -1, -2, -2, -1, 1]
    visited = [[[0] * (k + 1) for i in range(w)] for j in range(h)]
    for i in range(k+1):
        visited[0][0][i] = 1
    print(solution(0, 0))
