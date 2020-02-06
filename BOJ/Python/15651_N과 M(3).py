# baekjoon source = "https://www.acmicpc.net/problem/15651"

import sys

def solution(k):
    if k == m:
        print(*answer)
        return

    for i in range(1, n + 1):
        if not answer[k]:
            answer[k] = i
            solution(k + 1)
            answer[k] = 0

n, m = map(int, sys.stdin.readline().split())
answer = [0] * m
solution(0)
