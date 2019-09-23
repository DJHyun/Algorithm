# baekjoon source = "https://www.acmicpc.net/problem/1764"
import sys

N, M = map(int, sys.stdin.readline().split())
arr = set()
result = []

for i in range(N+M):
    check = sys.stdin.readline().strip()
    a = len(arr)+1
    arr.add(check)
    b = len(arr)
    if a != b:
        result.append(check)

result.sort()
print(N + M - len(arr))
print('\n'.join(result))
