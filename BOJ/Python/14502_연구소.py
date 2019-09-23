# baekjoon source = "https://www.acmicpc.net/problem/14502"
import sys

def solution(x, y):
    global cnt, result

    q = [[x, y]]
    visited[x][y] = cnt
    while q:
        t = q.pop(0)
        for i in range(4):
            tx = t[0] + dx[i]
            ty = t[1] + dy[i]
            if check(tx, ty) and cnt > visited[tx][ty]:
                visited[tx][ty] = cnt
                q.append([tx, ty])

def three(depth):
    global cnt, result

    if depth == 3:

        for i in range(n):
            for j in range(m):
                if arr[i][j] == 2:
                    solution(i, j)
        count = 0
        for i in visited:
            for j in i:
                if j < cnt:
                    count += 1

        for i in arr:
            print(i)
        print('--------------------------------')

        for i in visited_three:
            print(i)
        print()
        result = max(result, count - (go + 3))
        cnt += 1
        return

    for i in range(n):
        for j in range(m):
            print(i,j,arr[i][j])
            if arr[i][j] == 0 and depth < visited_three[i][j]:
                print("벽벽벽")
                arr[i][j] = 4
                visited_three[i][j] = depth+1
                three(depth + 1)
                print('asdfasdf',i,j)
                arr[i][j] = 0

def check(x, y):
    if x < 0 or x > n - 1: return False
    if y < 0 or y > m - 1: return False
    if arr[x][y] != 0: return False
    return True
q = [1,2,3]
print(q.pop(1))
print(q)
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
visited_three = [[float('inf')] * m for _ in range(n)]
cnt = 1
dx, dy = [0, 0, 1, -1], [-1, 1, 0, 0]
result = 0
go = 0

for i in arr:
    for j in i:
        if j == 1:
            go += 1

three(0)
print(result)
