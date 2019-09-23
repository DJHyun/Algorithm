# baekjoon source = "https://www.acmicpc.net/problem/16236"
'''
3
0 0 1
0 0 0
0 9 0
3

4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4
14

6
5 4 3 2 3 4
4 3 2 3 4 5
3 2 9 5 6 6
2 1 2 3 4 5
3 2 1 6 5 4
6 6 6 6 6 6
60

6
6 0 6 0 6 1
0 0 0 0 0 2
2 3 4 5 6 6
0 0 0 0 0 2
0 2 0 0 0 0
3 9 3 0 0 1
48
'''

def check(x, y):
    global visited

    if x < 0 or x > n - 1: return False
    if y < 0 or y > n - 1: return False
    if visited[x][y] == 1: return False
    return True

def solution(gogo, count):
    global visited
    tq = []
    tq.append(gogo)
    ch = 0
    cnt = 0
    up = 0
    result = 0
    c = 1
    food = []
    while cnt < count and tq:
        q = tq[:]
        tq.clear()
        while q:
            t = q.pop(0)
            visited[t[0]][t[1]] = 1
            for i in range(4):
                x = t[0] + dx[i]
                y = t[1] + dy[i]
                if check(x, y) and arr[x][y] <= t[2]:
                    if arr[x][y] == 0 or arr[x][y] == t[2]:
                        visited[x][y] = 1
                        tq.append([x, y, t[2]])
                    elif arr[x][y] < t[2]:
                        food.append([x,y])
            food.sort()
        for f in food:
            ch += 1
            checka[f[0]][f[1]] = ch
            arr[f[0]][f[1]] = 0
            cnt += 1
            if up + 1 == t[2]:
                up = 0
                t[2] += 1
            else:
                up += 1
            tq.clear()
            q.clear()
            result += c
            c = 0
            visited = [[0] * n for _ in range(n)]
            tq.append([f[0], f[1], t[2]])
            break
        food.clear()
        c += 1


    return result


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
checka = [[0]*n for _ in range(n)]
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
count = 0;
gogo = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            gogo.append(i)
            gogo.append(j)
            gogo.append(2)
            arr[i][j] = 0
        elif arr[i][j] != 9 and arr[i][j]:
            count += 1

print(solution(gogo, count))
