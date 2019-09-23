# baekjoon source = "https://www.acmicpc.net/problem/8958"
import sys

N, K = map(int,sys.stdin.readline().split())
medal = [[0]*3 for _ in range(N+1)]
for i in range(1, N+1):
    num = list(map(int,sys.stdin.readline().split()))
    medal[num[0]] = num[1:]

check = medal[K]
result = 1
for i in range(1, N + 1):
    if i != K:
        if check[0] < medal[i][0]:
            result += 1
        elif check[0] == medal[i][0] and check[1] < medal[i][1]:
            result += 1
        elif check[0] == medal[i][0] and check[1] == medal[i][1] and check[2] < medal[i][2]:
            result += 1
print(result)
