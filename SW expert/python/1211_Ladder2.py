# SW Expert Academy
import sys

sys.stdin = open('뭐지.txt', 'r')

def check(x, y):
    if x < 0 or x > 99: return False
    if y < 0 or y > 99: return False
    if arr[x][y] == 0: return False
    return True

def dfs(a):
    if a[0] == 99:
        return 1
    global cnt
    visited[a[0]][a[1]] = 1
    cnt += 1
    for i in range(4):
        x = dx[i] + a[0]
        y = dy[i] + a[1]
        if check(x, y) and not visited[x][y]:
            if dfs((x,y)):
                return 1

for _ in range(1, 11):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    st = []
    dx = [0, 0, 1]
    dy = [1, -1, 0]

    for i in range(len(arr[0])):
        if arr[0][i] == 1:
            st.append((0, i))

    # max_ = 10000000000
    # result = 0
    # for i in st:
    #     visited = [[0]*100 for _ in range(100)]
    #     cnt = 0
    #     dfs(i)
    #     if max_ > cnt:
    #         max_ = cnt
    #         result = i[1]
    #
    #

    max_,result = 1000000,0
    for i in st:
        visited = [[0] * 100 for _ in range(100)]
        x = i[0]
        y = i[1]
        cnt = 0
        flag = True
        while flag:
            cnt += 1
            visited[x][y] = 1
            for a in range(3):
                rx = dx[a] + x
                ry = dy[a] + y
                if check(rx, ry) and not visited[rx][ry]:
                    x = rx
                    y = ry
                    if x == 99:
                        flag = False
                        break

        if max_ > cnt:
            max_ = cnt
            result = i[1]

    print('#{} {}'.format(test_case, result))

