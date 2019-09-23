# baekjoon source = "https://www.acmicpc.net/problem/2573"
import sys

def check(x, y):
    if x < 0 or x > n - 1: return False
    if y < 0 or y > m - 1: return False
    if arr[x][y] == 0: return False
    return True

def solution(x, y):
    if x < 0 or x > n - 1: return False
    if y < 0 or y > m - 1: return False
    if arr[x][y] != 0: return False
    return True

def count(x, y):
    q = [[x, y]]
    visited[x][y] = result+1
    while q:
        t = q.pop(0)
        for i in range(4):
            tx = t[0] + dx[i]
            ty = t[1] + dy[i]
            if check(tx, ty) and result + 1 > visited[tx][ty]:
                visited[tx][ty] = result+1
                q.append([tx, ty])

n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
remove = [[0] * m for _ in range(n)]
result = 0
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
c = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] != 0:
            c += 1

result_flag = True
while result_flag:
    flag = False
    for i in range(n):
        if not result_flag:
            break;
        for j in range(m):
            if arr[i][j] != 0 and result+1 > visited[i][j]:
                if flag:
                    result_flag = False
                    result -= 1
                    break
                count(i, j)
                flag = True

    if result_flag:
        for i in range(n):
            for j in range(m):
                if arr[i][j] != 0:
                    remove[i][j] = result + 1
                    cnt = 0
                    for d in range(4):
                        x = i + dx[d]
                        y = j + dy[d]
                        if solution(x, y) and result+1 > remove[x][y]:
                            cnt += 1
                    if arr[i][j] - cnt <= 0:
                        arr[i][j] = 0
                        c -= 1
                    else:
                        arr[i][j] -= cnt

    result += 1
    if c == 0:
        result = 0
        break

print(result)
