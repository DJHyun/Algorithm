# baekjoon source = "https://www.acmicpc.net/problem/17780"

import sys

def check(x, y):
    if x < 0 or x > n - 1: return False
    if y < 0 or y > n - 1: return False
    if arr[x][y] == 2: return False
    return True

n, k = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
mal = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]
visited = [[[] for i in range(n)] for j in range(n)]

for i in range(k):
    mal[i][0] -= 1
    mal[i][1] -= 1

for v, i in enumerate(mal):
    visited[i[0]][i[1]].append(v)

result = 0
result_flag = False
while result <= 1000:

    for i in range(k):

        tx = mal[i][0]
        ty = mal[i][1]
        z = mal[i][2]
        if visited[tx][ty].index(i) != 0:
            continue
        flag = False
        c = 0
        if z == 1:
            if check(tx, ty + 1):
                mal[i][1] += 1
                start = visited[tx][ty].index(i)
                a = visited[tx][ty][:start]
                b = visited[tx][ty][start:]
                visited[tx][ty] = a
                c = 1
                if arr[tx][ty + 1] == 1:
                    b.reverse()
                    visited[tx][ty + 1] += b
                else:
                    visited[tx][ty + 1] += b
            else:
                flag = True

        elif z == 2:
            if check(tx, ty - 1):
                mal[i][1] -= 1
                start = visited[tx][ty].index(i)
                a = visited[tx][ty][:start]
                b = visited[tx][ty][start:]
                visited[tx][ty] = a
                c = 2
                if arr[tx][ty - 1] == 1:
                    b.reverse()
                    visited[tx][ty - 1] += b
                else:
                    visited[tx][ty - 1] += b
            else:
                flag = True

        elif z == 3:
            if check(tx - 1, ty):
                mal[i][0] -= 1
                start = visited[tx][ty].index(i)
                a = visited[tx][ty][:start]
                b = visited[tx][ty][start:]
                visited[tx][ty] = a
                c = 3
                if arr[tx - 1][ty] == 1:
                    b.reverse()
                    visited[tx - 1][ty] += b
                else:
                    visited[tx - 1][ty] += b
            else:
                flag = True
        elif z == 4:
            if check(tx + 1, ty):
                mal[i][0] += 1
                start = visited[tx][ty].index(i)
                a = visited[tx][ty][:start]
                b = visited[tx][ty][start:]
                visited[tx][ty] = a
                c = 4
                if arr[tx + 1][ty] == 1:
                    b.reverse()
                    visited[tx + 1][ty] += b
                else:
                    visited[tx + 1][ty] += b
            else:
                flag = True

        if flag:
            if z == 1:
                mal[i][2] = 2
                if check(tx, ty - 1):
                    mal[i][1] -= 1
                    start = visited[tx][ty].index(i)
                    a = visited[tx][ty][:start]
                    b = visited[tx][ty][start:]
                    visited[tx][ty] = a
                    c = 2
                    if arr[tx][ty - 1] == 1:
                        b.reverse()
                        visited[tx][ty - 1] += b
                    else:
                        visited[tx][ty - 1] += b
            elif z == 2:
                mal[i][2] = 1
                if check(tx, ty + 1):
                    mal[i][1] += 1
                    start = visited[tx][ty].index(i)
                    a = visited[tx][ty][:start]
                    b = visited[tx][ty][start:]
                    visited[tx][ty] = a
                    c = 1
                    if arr[tx][ty + 1] == 1:
                        b.reverse()
                        visited[tx][ty + 1] += b
                    else:
                        visited[tx][ty + 1] += b
            elif z == 3:
                mal[i][2] = 4
                if check(tx + 1, ty):
                    mal[i][0] += 1
                    start = visited[tx][ty].index(i)
                    a = visited[tx][ty][:start]
                    b = visited[tx][ty][start:]
                    visited[tx][ty] = a
                    c = 4
                    if arr[tx + 1][ty] == 1:
                        b.reverse()
                        visited[tx + 1][ty] += b
                    else:
                        visited[tx + 1][ty] += b
            elif z == 4:
                mal[i][2] = 3
                if check(tx - 1, ty):
                    mal[i][0] -= 1
                    start = visited[tx][ty].index(i)
                    a = visited[tx][ty][:start]
                    b = visited[tx][ty][start:]
                    visited[tx][ty] = a
                    c = 3
                    if arr[tx - 1][ty] == 1:
                        b.reverse()
                        visited[tx - 1][ty] += b
                    else:
                        visited[tx - 1][ty] += b

        if c == 1:
            ty += 1
        elif c == 2:
            ty -= 1
        elif c == 3:
            tx -= 1
        elif c == 4:
            tx += 1

        for j in visited[tx][ty]:
            mal[j][0] = tx
            mal[j][1] = ty

        if len(visited[tx][ty]) >= 4:
            result_flag = True
            break

    if result_flag:
        result += 1
        break

    result += 1
if result == 1001:
    print(-1)
else:
    print(result)
