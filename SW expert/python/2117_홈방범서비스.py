import sys

sys.stdin = open("2117_홈방범서비스.txt", "r")

def check(x, y):
    global n
    if x < 0 or x > n - 1: return False
    if y < 0 or y > n - 1: return False
    return True

def solution(x, y):
    global m,result, ans

    # print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',x,y)
    tq = []
    tq.append([x, y])
    visited = [[0] * n for _ in range(n)]
    visited[x][y] = 1
    home = 0
    k = 1

    while k <= (n * 2 - 1):
        # print('kkkkk',k)
        if k == 1:
            home = arr[x][y]
            money = home * m - (k * k + (k - 1) * (k - 1))
            # print('k=1',money)
            if money >= 0:
                if ans < home:
                    ans = home
            k += 1
        else:
            while tq:
                q = tq[:]
                tq.clear()
                while q:
                    t = q.pop(0)
                    for i in range(4):
                        tx = t[0] + dx[i]
                        ty = t[1] + dy[i]
                        if check(tx, ty) and not visited[tx][ty]:
                            tq.append([tx, ty])
                            visited[tx][ty] = 1
                            if arr[tx][ty] == 1:
                                home += 1

                # for i in visited:
                #     print(i)
                # print()
                money = (home*m) - (k*k + (k-1)*(k-1))
                # print('동',money,home)
                if money >= 0:
                    if ans < home:
                        ans = home

                # print("결과",result, ans)

                k += 1

            k+=1

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    result = 0
    ans = 0

    for i in range(n):
        for j in range(n):
            solution(i, j)

    print(f'#{test_case} {ans}')
