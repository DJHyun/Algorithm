# baekjoon source = "https://www.acmicpc.net/problem/11726"
import sys

def solution(s):
    if s == 1 or s == 0:
        return 1
    if memo[s] != 0:
        return memo[s]

    memo[s] = solution(s - 1) + solution(s - 2)
    return memo[s]

n = int(sys.stdin.readline())
memo = [0] * (n+1)
memo[0] = memo[1] = 1

solution(n)
print(memo[n]%10007)
