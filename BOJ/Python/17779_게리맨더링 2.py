# baekjoon source = "https://www.acmicpc.net/problem/17779"

import sys

def check(x, y):
    if x < 0 or x > n - 1: return False
    if y < 0 or y > n - 1: return False
    return True

def select(x, y):
    left = []
    right = []
    tx = x
    ty = y
    while True:
        tx += dx[0]
        ty += dy[0]
        if check(tx, ty):
            left.append([tx, ty])
        else:
            tx = x
            ty = y
            break

    while True:
        tx += dx[1]
        ty += dy[1]
        if check(tx, ty):
            right.append([tx, ty])
        else:
            break

    result = []
    for i in range(len(left)):
        check_left = []
        a = left[i][0]
        b = left[i][1]
        while True:
            a += dx[1]
            b += dy[1]
            if check(a, b):
                check_left.append([a, b])
            else:
                break
        for j in range(len(right)):
            a = right[j][0]
            b = right[j][1]
            while True:
                a += dx[0]
                b += dy[0]
                if check(a, b):
                    if [a, b] in check_left:
                        result.append([left[i], right[j], [a, b]])
                        break
                else:
                    break

    return result

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx, dy = [1, 1], [-1, 1]
candi = []
result = float('inf')
for i in range(0, n - 2):
    for j in range(1, n - 1):
        candi = select(i, j)
        for c in candi:
            count = [0] * 5
            visited = [[0] * n for _ in range(n)]
            visited[i][j] = 5
            for cc in range(3):
                visited[c[cc][0]][c[cc][1]] = 5
                if cc == 0:
                    x, y = i, j
                    while x != c[cc][0] and y != c[cc][1]:
                        x += 1
                        y -= 1
                        visited[x][y] = 5
                elif cc == 1:
                    x, y = i, j
                    while x != c[cc][0] and y != c[cc][1]:
                        x += 1
                        y += 1
                        visited[x][y] = 5
                else:
                    x, y = c[0][0], c[0][1]
                    while x != c[cc][0] and y != c[cc][1]:
                        x += 1
                        y += 1
                        visited[x][y] = 5

                    x, y = c[1][0], c[1][1]
                    while x != c[cc][0] and y != c[cc][1]:
                        x += 1
                        y -= 1
                        visited[x][y] = 5

            for a in range(n):
                flag = False
                for b in range(n):
                    if (a == i and b == j) or (a == c[2][0] and b == c[2][1]):
                        if visited[a][b] == 5:
                            continue
                    else:
                        if visited[a][b] == 5 and not flag:
                            flag = True
                            continue
                        elif visited[a][b] == 5 and flag:
                            flag = False
                            continue

                    if flag:
                        visited[a][b] = 5
                    else:
                        if a < c[0][0] and b <= j:
                            visited[a][b] = 1
                        elif a >= c[0][0] and b < c[2][1]:
                            visited[a][b] = 3
                        elif a <= c[1][0] and b > j:
                            visited[a][b] = 2
                        elif a > c[1][0] and b >= c[2][1]:
                            visited[a][b] = 4

            for a in range(n):
                for b in range(n):
                    if visited[a][b] == 1:
                        count[0] += arr[a][b]
                    elif visited[a][b] == 2:
                        count[1] += arr[a][b]
                    elif visited[a][b] == 3:
                        count[2] += arr[a][b]
                    elif visited[a][b] == 4:
                        count[3] += arr[a][b]
                    else:
                        count[4] += arr[a][b]

            # for v in visited:
            #     print(v)
            # print(i,j,count, max(count)-min(count))
            result = min(result, max(count)-min(count))
            # print()

print(result)