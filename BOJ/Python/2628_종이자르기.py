# baekjoon source = "https://www.acmicpc.net/problem/2628"
import sys

y, x = map(int, sys.stdin.readline().split())
cnt = int(sys.stdin.readline())
arr = [[0] * (y+(y-1)) for _ in range(x+(x-1))]
max_, y_m = 0, 0
one, zero = 0, 0
memo = []

for i in range(cnt):
    dot, num = map(int, sys.stdin.readline().split())
    if (dot, num) not in memo:
        if dot == 0:
            for j in range(len(arr[0])):
                arr[2*num-1][j] = 1
        else:
            for a in range(len(arr)):
                arr[a][2*num-1] = 1

    print(dot, num)
    for i in arr:
        print(i)
    print()

    memo.append((dot, num))

cou = 0
for a in range(len(arr[0])):
    if arr[0][a] == 0:
        cou += 1
    else:
        max_ = max(max_, cou)
        cou = 0
max_ = max(max_, cou)

cou = 0
for a in range(len(arr)):
    if arr[a][0] == 0:
        cou += 1
    else:
        y_m = max(y_m, cou)
        cou = 0
y_m = max(y_m, cou)

print((max_+1)//2 * (y_m+1)//2)
