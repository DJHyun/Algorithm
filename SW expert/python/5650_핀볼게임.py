import sys

sys.stdin = open("5650_핀볼게임.txt", "r")

def check(x, y, d):
    global n
    cnt = 0
    if arr[x][y] == 1:
        cnt += 1
        if d == 0:
            d = 1
        elif d == 1:
            d = 2
        elif d == 2:
            d = 3
        else:
            d = 0
    elif arr[x][y] == 2:
        cnt += 1
        if d == 0:
            d = 1
        elif d == 1:
            d = 3
        elif d == 2:
            d = 0
        else:
            d = 2
    elif arr[x][y] == 3:
        cnt += 1
        if d == 0:
            d = 3
        elif d == 1:
            d = 0
        elif d == 2:
            d = 1
        else:
            d = 2
    elif arr[x][y] == 4:
        cnt += 1
        if d == 0:
            d = 2
        elif d == 1:
            d = 0
        elif d == 2:
            d = 3
        else:
            d = 1
    elif arr[x][y] == 5:
        cnt += 1
        if d == 0:
            d = 1
        elif d == 1:
            d = 0
        elif d == 2:
            d = 3
        else:
            d = 2
    return [d, cnt]

def solution(x, d):
    global result

    q = []
    q.append(x)
    count = 0
    while q:
        t = q.pop(0)
        tx = t[0] + dx[d]
        ty = t[1] + dy[d]
        if tx == x[0] and ty == x[1]:
            result = max(result, count)
            return 0

        if tx < 0:
            d = 3
            count += 1
            q.append([tx, ty, d])
            continue
        elif tx > n - 1:
            d = 2
            count += 1
            q.append([tx, ty, d])
            continue
        elif ty < 0:
            d = 0
            count += 1
            q.append([tx, ty, d])
            continue
        elif ty > n - 1:
            d = 1
            count += 1
            q.append([tx, ty, d])
            continue

        if arr[tx][ty] == 6:
            for i in range(len(move)):
                if move[i][2] == 6 and (move[i][0] != tx or move[i][1] != ty):
                    tx = move[i][0]
                    ty = move[i][1]
                    break
        elif arr[tx][ty] == 7:
            for i in range(len(move)):
                if move[i][2] == 7 and (move[i][0] != tx or move[i][1] != ty):
                    tx = move[i][0]
                    ty = move[i][1]
                    break
        elif arr[tx][ty] == 8:
            for i in range(len(move)):
                if move[i][2] == 8 and (move[i][0] != tx or move[i][1] != ty):
                    tx = move[i][0]
                    ty = move[i][1]
                    break
        elif arr[tx][ty] == 9:
            for i in range(len(move)):
                if move[i][2] == 9 and (move[i][0] != tx or move[i][1] != ty):
                    tx = move[i][0]
                    ty = move[i][1]
                    break
        elif arr[tx][ty] == 10:
            for i in range(len(move)):
                if move[i][2] == 10 and move[i][0] != tx and move[i][1] != ty:
                    tx = move[i][0]
                    ty = move[i][1]
                    break

        xyz = check(tx, ty, d)

        if arr[tx][ty] == -1:
            result = max(result, count)
            return 0

        d = xyz[0]
        count += xyz[1]
        q.append([tx, ty, d])

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
    move = []
    end = []
    result = 0

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 6:
                move.append([i, j, 6])
            elif arr[i][j] == 7:
                move.append([i, j, 7])
            elif arr[i][j] == 8:
                move.append([i, j, 8])
            elif arr[i][j] == 9:
                move.append([i, j, 9])
            elif arr[i][j] == 10:
                move.append([i, j, 10])

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                for z in range(4):
                    solution([i, j], z)

    print(f'#{test_case} {result}')
