# baekjoon source = "https://www.acmicpc.net/problem/16988"

import sys
from collections import deque

def check(x, y):
    if x < 0 or x > n - 1: return False
    if y < 0 or y > m - 1: return False
    if check_visited[x][y]: return False
    return True

def solution(x):
    global flag, result, score

    check_visited[x[0]][x[1]] = 1
    q = deque([[x[0], x[1]]])
    s_score = 1
    flag = True
    while q:
        t = q.popleft()
        for i in range(4):
            tx = t[0] + dx[i]
            ty = t[1] + dy[i]
            if check(tx, ty) and not check_visited[tx][ty]:
                if arr[tx][ty] == 0:
                    flag = False
                if arr[tx][ty] == 2:
                    s_score += 1
                    q.append([tx, ty])
                    check_visited[tx][ty] = 1
    if flag:
        return s_score
    return 0

n, m = map(int, sys.stdin.readline().split())
arr = [[0] * m for _ in range(n)]
check_two = []
for i in range(n):
    input_ = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        arr[i][j] = input_[j]
        if arr[i][j] == 2:
            check_two.append([i, j])
visited = [[0] * m for _ in range(n)]
result = 0

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

for i in range(n):
    for j in range(m):
        if not arr[i][j] and not visited[i][j]:
            arr[i][j] = 1
            visited[i][j] = 1
            for a in range(n):
                for b in range(m):
                    if not arr[a][b] and (i != a or j != b) and not visited[a][b]:
                        arr[a][b] = 1
                        score = 0
                        flag = True
                        check_visited = [[0] * m for _ in range(n)]
                        for c in check_two:
                            if not check_visited[c[0]][c[1]]:
                                s_score = solution(c)
                                score += s_score

                        result = max(result, score)
                        arr[a][b] = 0
            arr[i][j] = 0
print(result)
