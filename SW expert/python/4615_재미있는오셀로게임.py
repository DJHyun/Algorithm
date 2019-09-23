import sys

'''
1이면 흑돌, 2이면 백돌
'''
sys.stdin = open("4615_재미있는오셀로게임.txt", "r")


def check(x, y):
    if x < 0 or x > N - 1: return False
    if y < 0 or y > N - 1: return False
    return True


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    dx, dy = [1, -1, 1, -1], [1, -1, -1, 1]
    da, db = [0, 0, 1, -1], [1, -1, 0, 0]
    arr[N // 2][N // 2] = 2
    arr[N // 2][N // 2 - 1] = 1
    arr[N // 2 - 1][N // 2] = 1
    arr[N // 2 - 1][N // 2 - 1] = 2

    for _ in range(M):
        x, y, a = map(int, input().split())

        xflag = [True] * 4
        yflag = [True] * 4

        x -= 1
        y -= 1

        arr[x][y] = a

        for j in range(1, N):
            for i in range(4):
                if xflag[i]:
                    dd = x + (da[i] * j)
                    ddy = y + (db[i] * j)
                    if check(dd, ddy):
                        if arr[dd][ddy] == 0:
                            xflag[i] = False
                        elif arr[dd][ddy] == a:
                            if i == 0:
                                for b in range(y, ddy + 1):
                                    arr[x][b] = a
                            elif i == 1:
                                for b in range(ddy, y + 1):
                                    arr[x][b] = a
                            elif i == 2:
                                for b in range(x, dd + 1):
                                    arr[b][y] = a
                            else:
                                for b in range(dd, x + 1):
                                    arr[b][y] = a
                            xflag[i] = False

                if yflag[i]:
                    dd = x + (dx[i] * j)
                    ddy = y + (dy[i] * j)
                    if check(dd, ddy):
                        if arr[dd][ddy] == 0:
                            yflag[i] = False
                        elif arr[dd][ddy] == a:
                            if i == 0:
                                for b in range(j, 0, -1):
                                    arr[x + dx[i] * b][y + dy[i] * b] = a
                            elif i == 1:
                                for b in range(j, 0, -1):
                                    arr[x + dx[i] * b][y + dy[i] * b] = a
                            elif i == 2:
                                for b in range(j, 0, -1):
                                    arr[x + dx[i] * b][y + dy[i] * b] = a
                            elif i == 3:
                                for b in range(j, 0, -1):
                                    arr[x + dx[i] * b][y + dy[i] * b] = a
                            yflag[i] = False

        print(x, y)
        for i in arr:
            print(i)
        print()

    one, two = 0, 0
    for i in arr:
        for j in i:
            if j == 1:
                one += 1
            elif j == 2:
                two += 1

    print('#{} {} {}'.format(test_case, one, two))
