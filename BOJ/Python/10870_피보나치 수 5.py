# baekjoon source = "https://www.acmicpc.net/problem/10870"
import sys

def solution(x):
    if x == 0:
        return 0

    if x == 1:
        return 1

    if memo[x] != 0:
        return memo[x]

    memo[x] = solution(x - 1) + solution(x - 2)
    return memo[x]

n = int(sys.stdin.readline())
if n == 0:
    print(0)
else:
    memo = [0] * (n + 1)
    memo[1] = 1
    print(solution(n))
