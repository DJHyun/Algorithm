import sys

sys.stdin = open("격자판의숫자이어붙이기.txt", "r")

def check(x, y):
    if x < 0 or x > 3: return False
    if y < 0 or y > 3: return False
    return True

def bfs(x):
    tq = []
    cnt = 0
    tq.append(x)

    while tq:
        q = tq[:]
        tq.clear()
        cnt += 1
        while q:
            t = q.pop(0)
            for i in range(4):
                tx = t[0] + dx[i]
                ty = t[1] + dy[i]
                if check(tx, ty):
                    tq.append([tx, ty, t[2] + arr[tx][ty]])
                    if len(t[2] + arr[tx][ty]) == 7 and t[2] + arr[tx][ty] not in result:
                        result.append(t[2] + arr[tx][ty])

        if cnt == 6:
            break


T = int(input())
for test_case in range(1, T + 1):
    arr = [input().split() for _ in range(4)]
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    result = []

    for i in range(4):
        for j in range(4):
            v = bfs([i, j, arr[i][j]])

    print(f'#{test_case} {len(result)}')
