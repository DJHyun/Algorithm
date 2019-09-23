# baekjoon source = "https://www.acmicpc.net/problem/2636"
import sys

def check(d):
    x = d // 100
    y = d % 100
    if x < 0 or x > n - 1: return False
    if y < 0 or y > m - 1: return False
    if arr[x][y] == 1: return False
    return True

def solution(t):
    visited = [[0] * m for _ in range(n)]
    q = [t]
    visited[t // 100][t % 100] = 1

    while q:
        t = q.pop(0)
        x = t // 100
        y = t % 100
        for i in range(4):
            x_ = x + dx[i]
            y_ = y + dy[i]
            if check(x_ * 100 + y_) and not visited[x_][y_]:
                if x_ == 0 or x_ == n - 1 or y_ == 0 or y_ == m - 1:
                    return True
                visited[x_][y_] = 1
                q.append(x_ * 100 + y_)

n, m = map(int, sys.stdin.readline().split())
arr = [[0]*m for _ in range(n)]
cnt = 0
for i in range(n):
    number = list(map(int,sys.stdin.readline().split()))
    for j in range(m):
        if number[j] == 1:
            cnt += 1
        arr[i][j] = number[j]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
result = 0
check_cnt = cnt

while True:
    remove = [[0] * m for _ in range(n)]
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if arr[i][j] == 1:
                for a in range(4):
                    x = i + dx[a]
                    y = j + dy[a]
                    if check(x * 100 + y):
                        if solution(x * 100 + y):
                            cnt -= 1
                            remove[i][j] = 1
                            break

    for i in range(n):
        for j in range(m):
            if remove[i][j] == 1:
                arr[i][j] = 0

    result += 1
    if cnt != 0:
        check_cnt = cnt
    else:
        break

print(result)
print(check_cnt)

