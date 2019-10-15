# baekjoon source = "https://www.acmicpc.net/problem/16985"
import sys
from collections import deque

def permutations(depth):
    if depth == 5:
        in_permutations(0)
        return
    for i in range(5):
        flag = False
        if not visited[i]:
            if depth == 0:
                for c in range(4):
                    if check(arr[i],c)[0][0] == 1:
                        flag = True
                        break
                if flag:
                    visited[i] = 1
                    p[depth] = i
                    permutations(depth + 1)
                    visited[i] = 0
            else:
                visited[i] = 1
                p[depth] = i
                permutations(depth + 1)
                visited[i] = 0


def in_permutations(depth):
    global v
    if depth == 5:

        for go in range(5):
            for do in range(5):
                result_arr[go][do] = arr[p[go]][do][:]

        for go in range(5):
            result_arr[go] = check(result_arr[go],inp[go])

        if result_arr[0][0][0] == 1 and result_arr[4][4][4] == 1:
            v = [[[0] * 5 for _ in range(5)] for _ in range(5)]
            bfs(0, 0, 0, 0)
        return

    for i in range(4):
        inp[depth] = i
        in_permutations(depth + 1)

def check(x,number):
    if number == 0:
        return x

    for i in range(1):
        for j in range(number*4):
            x[i][j%4], x[j%4][4-i], x[4-i][4-(j%4)], x[4-(j%4)][i] = x[4-(j%4)][i],x[i][j%4],x[j%4][4-i], x[4-i][4-(j%4)]

    for j in range(number):
        x[1][1],x[1][3],x[3][3],x[3][1] = x[3][1],x[1][1],x[1][3],x[3][3]
        x[1][2],x[2][3],x[3][2],x[2][1] = x[2][1],x[1][2],x[2][3],x[3][2]

    return x

def error(x,y,z):
    if x < 0 or x > 4: return False
    if y < 0 or y > 4: return False
    if z < 0 or z > 4: return False
    return True

def bfs(x,y,z,score):
    global r
    q = deque([[x,y,z,score]])
    v[z][x][y] = 1

    while q:
        t = q.popleft()
        for j in range(4):
            tx = t[0] + dx[j]
            ty = t[1] + dy[j]
            tz = t[2]
            if error(tx, ty, tz) and result_arr[tz][tx][ty] and not v[tz][tx][ty]:
                if tz == 4 and tx == 4 and ty == 4:
                    r = min(r, t[3] + 1)
                elif t[3] + 1 < r:
                    v[tz][tx][ty] = 1
                    q.append([tx, ty, tz, t[3] + 1])

        for j in range(2):
            tx = t[0]
            ty = t[1]
            tz = t[2] + dz[j]
            if error(tx, ty, tz) and result_arr[tz][tx][ty] and not v[tz][tx][ty]:
                if tz == 4 and tx == 4 and ty == 4:
                    r = min(r, t[3] + 1)
                elif t[3] + 1 < r:
                    v[tz][tx][ty] = 1
                    q.append([tx, ty, tz, t[3] + 1])

arr = [[0] * 5 for _ in range(5)]
result_arr = [[[0]*5 for _ in range(5)] for _ in range(5)]
v = [[[0]*5 for _ in range(5)] for _ in range(5)]
p = [0] * 5
inp = [0] * 5
visited = [0] * 6
dx, dy, dz = [0, 0, 1, -1], [1, -1, 0, 0], [1,-1]
r = float('inf')

for i in range(5):
    for j in range(5):
        arr[i][j] = list(map(int, sys.stdin.readline().split()))

permutations(0)
if r == float('inf'):
    r = -1
print(r)