# baekjoon source = "https://www.acmicpc.net/problem/2667"
'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''
import sys

def check(x, y):
    if x < 0 or x > N - 1: return False
    if y < 0 or y > N - 1: return False
    if arr[x][y] == 0: return False
    return True

def bfs(a):
    p = []
    p.append(a)
    arr[a[0]][a[1]] = 0
    count = 0
    while p:
        count += 1
        t = p.pop(0)
        for i in range(4):
            if check(t[0] + dx[i], t[1] + dy[i]):
                p.append((t[0] + dx[i], t[1] + dy[i]))
                arr[t[0] + dx[i]][t[1] + dy[i]] = 0

    return count

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
cnt = 0
count = []

for i in range(N):
    for j in range(N):
        if arr[i][j]:
            count.append(bfs((i, j)))
            cnt += 1

print(cnt)
count.sort()
for i in range(cnt):
    print(count[i])
