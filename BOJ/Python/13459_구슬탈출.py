# baekjoon source = "https://www.acmicpc.net/problem/13459"
import copy

def check(b, x, y):
    if b[x][y] != '.': return False
    return True

def up(b, x, y, q, w):
    while check(b, x - 1, y) or check(b, q - 1, w):
        if check(b, x - 1, y):
            b[x - 1][y], b[x][y] = b[x][y], b[x - 1][y]
            x -= 1

        if check(b, q - 1, w):
            b[q - 1][w], b[q][w] = b[q][w], b[q - 1][w]
            q -= 1

    if arr[x - 1][y] == 'O':
        x = x - 1
    if arr[q - 1][w] == 'O':
        q = q - 1
    return [x, y, q, w]

def down(b, x, y, q, w):
    while check(b, x + 1, y) or check(b, q + 1, w):
        if check(b, x + 1, y):
            b[x + 1][y], b[x][y] = b[x][y], b[x + 1][y]
            x += 1

        if check(b, q + 1, w):
            b[q + 1][w], b[q][w] = b[q][w], b[q + 1][w]
            q += 1

    if arr[x + 1][y] == 'O':
        x = x + 1
    if arr[q + 1][w] == 'O':
        q = q + 1
    return [x, y, q, w]

def left(b, x, y, q, w):
    while check(b, x, y - 1) or check(b, q, w - 1):
        if check(b, x, y - 1):
            b[x][y - 1], b[x][y] = b[x][y], b[x][y - 1]
            y -= 1

        if check(b, q, w - 1):
            b[q][w - 1], b[q][w] = b[q][w], b[q][w - 1]
            w -= 1
    if arr[x][y - 1] == 'O':
        y -= 1
    if arr[q][w - 1] == 'O':
        w = w - 1
    return [x, y, q, w]

def right(b, x, y, q, w):
    while check(b, x, y + 1) or check(b, q, w + 1):
        if check(b, x, y + 1):
            b[x][y + 1], b[x][y] = b[x][y], b[x][y + 1]
            y += 1

        if check(b, q, w + 1):
            b[q][w + 1], b[q][w] = b[q][w], b[q][w + 1]
            w += 1

    if arr[x][y + 1] == 'O':
        y += 1
    if arr[q][w + 1] == 'O':
        w = w + 1

    return [x, y, q, w]

def solution(a, x, y, q, w, k, d, udlr):
    global flag

    # for i in a:
    #     print(i)
    # print()

    if arr[q][w] == 'O':
        return

    if arr[x][y] == 'O':
        flag = True
        if udlr == 'u':
            while a[q - 1][w] == '.' or a[q - 1][w] == 'R':
                q -= 1
            if a[q - 1][w] == 'O':
                flag = False
        elif udlr == 'd':
            while a[q + 1][w] == '.' or a[q + 1][w] == 'R':
                q += 1
            if a[q + 1][w] == 'O':
                flag = False
        elif udlr == 'l':
            while a[q][w - 1] == '.' or a[q][w - 1] == 'R':
                w -= 1
            if a[q][w - 1] == 'O':
                flag = False
        else:
            while a[q][w + 1] == '.' or a[q][w + 1] == 'R':
                w += 1
            if a[q][w + 1] == 'O':
                flag = False

        return

    if k == d:
        return

    for i in range(4):
        if udlr == 'u':
            if i == 1:
                go = copy.deepcopy(a)
                xy = down(go, x, y, q, w)
                solution(go, xy[0], xy[1], xy[2], xy[3], k + 1, d, 'd')
            elif i == 2:
                go = copy.deepcopy(a)
                xy = left(go, x, y, q, w)
                solution(go, xy[0], xy[1], xy[2], xy[3], k + 1, d, 'l')
            elif i == 3:
                go = copy.deepcopy(a)
                xy = right(go, x, y, q, w)
                solution(go, xy[0], xy[1], xy[2], xy[3], k + 1, d, 'r')
        elif udlr == 'd':
            if i == 0:
                go = copy.deepcopy(a)
                xy = up(go, x, y, q, w)
                solution(go, xy[0], xy[1], xy[2], xy[3], k + 1, d, 'u')
            elif i == 2:
                go = copy.deepcopy(a)
                xy = left(go, x, y, q, w)
                solution(go, xy[0], xy[1], xy[2], xy[3], k + 1, d, 'l')
            elif i == 3:
                go = copy.deepcopy(a)
                xy = right(go, x, y, q, w)
                solution(go, xy[0], xy[1], xy[2], xy[3], k + 1, d, 'r')
        elif udlr == 'l':
            if i == 0:
                go = copy.deepcopy(a)
                xy = up(go, x, y, q, w)
                solution(go, xy[0], xy[1], xy[2], xy[3], k + 1, d, 'u')
            elif i == 1:
                go = copy.deepcopy(a)
                xy = down(go, x, y, q, w)
                solution(go, xy[0], xy[1], xy[2], xy[3], k + 1, d, 'd')
            elif i == 3:
                go = copy.deepcopy(a)
                xy = right(go, x, y, q, w)
                solution(go, xy[0], xy[1], xy[2], xy[3], k + 1, d, 'r')
        elif udlr == 'r':
            if i == 0:
                go = copy.deepcopy(a)
                xy = up(go, x, y, q, w)
                solution(go, xy[0], xy[1], xy[2], xy[3], k + 1, d, 'u')
            elif i == 1:
                go = copy.deepcopy(a)
                xy = down(go, x, y, q, w)
                solution(go, xy[0], xy[1], xy[2], xy[3], k + 1, d, 'd')
            elif i == 2:
                go = copy.deepcopy(a)
                xy = left(go, x, y, q, w)
                solution(go, xy[0], xy[1], xy[2], xy[3], k + 1, d, 'l')
        else:
            if i == 0:
                go = copy.deepcopy(a)
                xy = up(go, x, y, q, w)
                solution(go, xy[0], xy[1], xy[2], xy[3], k + 1, d, 'u')
            elif i == 1:
                go = copy.deepcopy(a)
                xy = down(go, x, y, q, w)
                solution(go, xy[0], xy[1], xy[2], xy[3], k + 1, d, 'd')
            elif i == 2:
                go = copy.deepcopy(a)
                xy = left(go, x, y, q, w)
                solution(go, xy[0], xy[1], xy[2], xy[3], k + 1, d, 'l')
            elif i == 3:
                go = copy.deepcopy(a)
                xy = right(go, x, y, q, w)
                solution(go, xy[0], xy[1], xy[2], xy[3], k + 1, d, 'r')
        if flag:
            return

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
flag = False
# print(n, m)
# for i in arr:
#     print(i)
# print()

dis = [0, 0, 0, 0]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            dis[0] = i
            dis[1] = j
        elif arr[i][j] == 'B':
            dis[2] = i
            dis[3] = j

solution(arr, dis[0], dis[1], dis[2], dis[3], 0, 10, "")

if flag:
    print(1)
else:
    print(0)
