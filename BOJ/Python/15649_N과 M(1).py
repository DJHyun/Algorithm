# baekjoon source = "https://www.acmicpc.net/problem/15649"


# def solution(k):
#     if k == m:
#         print(*answer)
#         return
#
#     for i in range(1, n + 1):
#         if not visited[i]:
#             visited[i] = i
#             answer[k] = i
#             solution(k + 1)
#             visited[i] = 0
#             answer[k] = 0
#
# n, m = map(int, sys.stdin.readline().split())
# visited = [0] * (n + 1)
# answer = [0] * m
# solution(0)


import sys
import itertools

n, m = map(int, sys.stdin.readline().split())

for it in itertools.permutations(range(1, n + 1), m):
    print(*it)