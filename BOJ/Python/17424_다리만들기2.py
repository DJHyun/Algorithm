# baekjoon source = "https://www.acmicpc.net/problem/17424"

'''
6 10
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 1 0 0 0
1 0 1 0 0 0 1 0 0 1
1 0 1 0 0 0 1 0 0 1
0 0 1 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1

2
'''
import sys
from collections import deque

def check(x, y):
    if x < 0 or x > n - 1: return False
    if y < 0 or y > m - 1: return False
    return True

def get_label(x, y):
    global label

    q = deque([[x, y]])
    while q:
        t = q.popleft()
        for i in range(4):
            tx = t[0] + dx[i]
            ty = t[1] + dy[i]
            if check(tx, ty) and arr[tx][ty] == 1 and not visited[tx][ty]:
                visited[tx][ty] = 1
                arr[tx][ty] = label
                q.append([tx, ty])

def get_distance(x, y):
    global label

    q = deque([[x, y]])
    while q:
        t = q.popleft()
        for i in range(4):
            tx = t[0] + dx[i]
            ty = t[1] + dy[i]
            if check(tx, ty) and not arr[tx][ty]:
                d = 1
                while True:
                    tx += dx[i]
                    ty += dy[i]
                    if check(tx, ty):
                        if not arr[tx][ty]:
                            d += 1
                        else:
                            if arr[tx][ty] != arr[x][y]:
                                if d >= 2:
                                    if d < distacne[arr[x][y]][arr[tx][ty]]:
                                        distacne[arr[x][y]][arr[tx][ty]]= min(d, distacne[arr[x][y]][arr[tx][ty]])
                                        distacne[arr[tx][ty]][arr[x][y]] = min(d, distacne[arr[tx][ty]][arr[x][y]])
                                        test.append([arr[x][y],arr[tx][ty],d])
                                break
                            else:
                                break
                    else:
                        break

def find(x):
    if mst[x] == x:
        return x
    return find(mst[x])

def union(a):
    global result
    x = find(a[0])
    y = find(a[1])

    if x == y:
        return

    result += a[2]
    mst[y] = x


n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
visited = [[0] * m for _ in range(n)]

label = 1
for i in range(n):
    for j in range(m):
        if arr[i][j] and not visited[i][j]:
            visited[i][j] = 1
            arr[i][j] = label
            get_label(i, j)
            label += 1

distacne = [[float('inf')] * label for _ in range(label)]
test = []
for i in range(n):
    for j in range(m):
        if arr[i][j]:
            get_distance(i, j)

test = sorted(test, key=lambda x: x[2])
result = 0
mst = [i for i in range(label)]
for i in test:
    union(i)

standard = -1
for i in range(1,label):
    f = find(mst[i])
    if standard == -1:
        standard = f
    else:
        if standard != f:
            result = -1
            break
print(result)
