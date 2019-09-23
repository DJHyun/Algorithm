# baekjoon source = "https://www.acmicpc.net/problem/14503"

def check(x, y):
    if x < 0 or x > n - 1: return False
    if y < 0 or y > m - 1: return False
    if arr[x][y] == 1 or arr[x][y] == 2: return False
    return True

def back(x, y):
    if x < 0 or x > n - 1: return False
    if y < 0 or y > m - 1: return False
    if arr[x][y] == 1: return False
    return True

def direction(a):
    if a == 0:
        return [[0, 1, 0, -1], [-1, 0, 1, 0], [3, 2, 1, 0]]
    elif a == 1:
        return [[-1, 0, 1, 0], [0, -1, 0, 1], [0, 3, 2, 1]]
    elif a == 2:
        return [[0, -1, 0, 1], [1, 0, -1, 0], [1, 0, 3, 2]]
    else:
        return [[1, 0, -1, 0], [0, 1, 0, -1], [2, 1, 0, 3]]

def solution(x, y, d):
    q = [[x, y, d]]
    result = 0
    while q:
        t = q.pop(0)
        if arr[t[0]][t[1]] == 0:
            result += 1
            arr[t[0]][t[1]] = 2
        dd = direction(t[2])
        dx, dy, ddd = dd[0], dd[1], dd[2]
        for i in range(4):
            tx = t[0] + dx[i]
            ty = t[1] + dy[i]
            if check(tx, ty):
                q.append([tx, ty, ddd[i]])
                break
        else:
            if t[2] == 0:
                t[0] += 1
            elif t[2] == 1:
                t[1] -= 1
            elif t[2] == 2:
                t[0] -= 1
            else:
                t[1] += 1
            if back(t[0], t[1]):
                q.append([t[0], t[1], t[2]])

    return result

n, m = map(int, input().split())
x, y, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

print(solution(x, y, d))
