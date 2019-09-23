# baekjoon source = "https://www.acmicpc.net/problem/2578"
'''
11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18
5 10 7 16 2
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15
'''
import sys

def check_fun():
    cnt = 0
    for i in range(5):
        if arr[i].count(0) == 5:
            cnt += 1
    if cnt >= 3:
        return True
    for i in range(5):
        for j in range(5):
            if arr[j][i] == 0:
                if j == 4:
                    cnt += 1
            else:
                break

    if cnt >= 3:
        return True
    for i in range(5):
        if arr[i][i] == 0:
            if i == 4:
                cnt += 1
        else:
            break
    if cnt >= 3:
        return True

    for i in range(4, -1, -1):
        if arr[i][4 - i] == 0:
            if i == 0:
                cnt += 1
        else:
            break
    if cnt >= 3:
        return True

    return False


arr = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
check = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
flag = True
count = 0

for i in range(5):
    if flag:
        for j in range(5):
            if flag:
                for a in range(5):
                    if check[i][j] in arr[a]:
                        idx = arr[a].index(check[i][j])
                        arr[a][idx] = 0
                        count += 1
                        break
                if count >= 12:
                    if check_fun():
                        print(count)
                        flag = False
                        break