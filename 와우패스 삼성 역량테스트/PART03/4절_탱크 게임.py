'''
2
7
E 0 T 0 E E 0
0 B B 0 B 0 0
E B E 0 B T E
B B 0 T B 0 E
E T E 0 B 0 0
0 E 0 E B 0 T
0 0 B B B B E
5
E 0 T 0 E
0 B B 0 B
E B E 0 B
B B 0 T B
E T E 0 B
'''
from collections import deque

def check(x, y):
    if x < 0 or x > n - 1: return False
    if y < 0 or y > n - 1: return False
    if visited[x][y] == 1: return False
    return True

def solution(x, y):
    global result

    q = deque([[x, y]])
    while q:
        t = q.popleft()
        for i in range(4):
            tx = t[0] + dx[i]
            ty = t[1] + dy[i]
            if check(tx, ty):
                if arr[tx][ty] == 'E':
                    result += 1
                    visited[tx][ty] = 1
                    continue

                while arr[tx][ty] == '0':
                    tx += dx[i]
                    ty += dy[i]
                    if not check(tx,ty):
                        break
                    if arr[tx][ty] == 'E':
                        result += 1
                        visited[tx][ty] = 1



t = int(input())
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
for tc in range(1, t + 1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    our = []
    result = 0
    for i in range(n):
        input_ = list(input().strip().split())
        for j in range(n):
            arr[i][j] = input_[j]
            if input_[j] == 'T':
                our.append([i, j])

    for i in our:
        visited[i[0]][i[1]] = 1
        solution(i[0], i[1])

    print('#{} {}'.format(tc,result))