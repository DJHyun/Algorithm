# baekjoon source = "https://www.acmicpc.net/problem/10157"
'''
7 6
11
'''
import sys

y, x = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
arr = [[0] * y for _ in range(x)]
flag = 1
i = 1
x_i, y_i = -1, 0

while i < x * y + 1:
    if flag == 1:
        x_i += 1
        if x_i >= x - 1 or arr[x_i + 1][y_i] != 0:
            flag = 2
    elif flag == 2:
        y_i += 1
        if y_i >= y - 1 or arr[x_i][y_i + 1] != 0:
            flag = 3
    elif flag == 3:
        x_i -= 1
        if x_i <= 0 or arr[x_i - 1][y_i] != 0:
            flag = 4
    else:
        y_i -= 1
        if y_i <= 0 or arr[x_i][y_i - 1] != 0:
            flag = 1

    arr[x_i][y_i] = i
    i += 1

for i in range(x):
    if k in arr[i]:
        print(arr[i].index(k) + 1, i + 1)
        break
else:
    print(0)
