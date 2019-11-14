# baekjoon source = "https://www.acmicpc.net/problem/17845"
'''
80 3
650 40
700 60
60 40
'''
import sys

def solution(pos, cap):
    if pos == k or cap == 0:
        return 0
    ret = memo[pos][cap]

    if ret != -1:
        return ret

    if sub[pos][1] <= cap:
        ret = solution(pos + 1, cap - sub[pos][1]) + sub[pos][0]
    ret = max(ret, solution(pos + 1, cap))
    memo[pos][cap] = ret

    return ret

n, k = map(int, sys.stdin.readline().split())
memo = [[-1] * (n + 1) for _ in range(k)]
sub = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]

print(solution(0, n))
