# baekjoon source = "https://www.acmicpc.net/problem/17822"
import sys
from collections import deque

def check(x, y):
    if x < 0 or x > n - 1: return False
    if y < -1 or y > m: return False
    if visited[x][y % m] == 1: return False
    return True


def solution(x, y):
    global m
    q = deque([[x, y]])
    flag = False
    while q:
        t = q.popleft()
        for i in range(4):
            tx = t[0] + dx[i]
            ty = t[1] + dy[i]
            if check(tx, ty):
                if arr[x][y] == arr[tx][ty % m]:
                    flag = True
                    arr[tx][ty % m] = 0
                    visited[tx][ty % m] = 1
                    q.append([tx, ty % m])

    if flag:
        arr[x][y] = 0

    return flag

n, m, t = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
t_arr = [list(map(int, sys.stdin.readline().split())) for _ in range(t)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

for i in t_arr:
    c = i[0]
    for j in range(n):
        if not (j + 1) % c:
            if i[1] == 0:
                new_arr = [0] * m
                for a in range(m):
                    new_arr[(a + i[2]) % m] = arr[j][a]
                arr[j] = new_arr
            if i[1] == 1:
                new_arr = [0] * m
                for a in range(m):
                    new_arr[a - i[2]] = arr[j][a]
                arr[j] = new_arr

    result_flag = False
    visited = [[0] * m for _ in range(n)]
    for a in range(n):
        for b in range(m):
            if arr[a][b] != 0:
                visited[a][b] = 1
                if not result_flag:
                    result_flag = solution(a, b)
                else:
                    solution(a, b)

    result = 0
    for a in range(n):
        result += sum(arr[a])

    if not result_flag:
        count = 0
        for a in range(n):
            for b in range(m):
                if arr[a][b]:
                    count += 1
        if count > 0:
            avg = result / count
            for a in range(n):
                for b in range(m):
                    if not arr[a][b]:
                        continue
                    if arr[a][b] > avg:
                        arr[a][b] -= 1
                    elif arr[a][b] < avg:
                        arr[a][b] += 1

result = 0
for a in range(n):
    result += sum(arr[a])

print(result)
