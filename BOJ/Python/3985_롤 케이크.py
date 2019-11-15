# baekjoon source = "https://www.acmicpc.net/problem/3985"

import sys

l = int(sys.stdin.readline())
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

cake = [0] * (l + 1)

result = 0
size = 0
result_one = 0
size_one = 0
for i in range(n):
    cnt = 0
    a,b = arr[i][0],arr[i][1]
    if size_one < b-a:
        size_one = b -a
        result_one = (i+1)
    for j in range(a, b + 1):
        if not cake[j]:
            cake[j] = (i + 1)
            cnt += 1

    if cnt > size:
        size = cnt
        result = (i+1)

print(result_one)
print(result)
