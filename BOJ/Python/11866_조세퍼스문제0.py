# baekjoon source = "https://www.acmicpc.net/problem/11866"
import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(range(1, N + 1))
M -= 1

print('<',end='')
while arr:
    for i in range(M):
        arr.append(arr.pop(0))
    if len(arr) == 1:
        print(arr.pop(0), end='')
    else:
        print(arr.pop(0), end= ', ')
print('>',end='')