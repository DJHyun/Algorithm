# baekjoon source = "https://www.acmicpc.net/problem/5427"

import sys
from collections import deque

def check(x, y):
    if x < 0 or x > h - 1: return False
    if y < 0 or y > w - 1: return False
    return True

def solution(x, y):
    q = deque([[x, y]])
    f = deque(fire)

    cnt = 1
    while q:
        len_f = len(f)
        for i in range(len_f):
            t = f.popleft()
            for j in range(4):
                tx = t[0] + dx[j]
                ty = t[1] + dy[j]
                if check(tx, ty) and arr[tx][ty] != '#' and visited[tx][ty] != 2:
                    f.append([tx, ty])
                    arr[tx][ty] = '*'
                    visited[tx][ty] = 2

        len_q = len(q)
        for j in range(len_q):
            t = q.popleft()
            for i in range(4):
                tx = t[0] + dx[i]
                ty = t[1] + dy[i]
                if check(tx, ty) and arr[tx][ty] == '.' and visited[tx][ty] == 0:
                    if tx == 0 or tx == h - 1 or ty == 0 or ty == w - 1:
                        return cnt + 1
                    q.append([tx, ty])
                    visited[tx][ty] = 1
                    arr[tx][ty] = '@'
        cnt += 1

    return 'IMPOSSIBLE'

t = int(sys.stdin.readline().strip())
for _ in range(t):
    w, h = map(int, sys.stdin.readline().strip().split())
    arr = [list(sys.stdin.readline().strip()) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    fire = []
    go = []
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

    for i in range(h):
        for j in range(w):
            if arr[i][j] == '@':
                go.append([i, j])
            elif arr[i][j] == '*':
                fire.append([i, j])

    x = go[0][0]
    y = go[0][1]
    if x == 0 or x == h - 1 or y == 0 or y == w - 1:
        print(1)
    else:
        print(solution(x, y))
