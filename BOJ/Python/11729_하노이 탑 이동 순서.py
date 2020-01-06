# baekjoon source = "https://www.acmicpc.net/problem/11729"

import sys

def solution(n, x, y):
    global cnt

    if n == 0: return
    solution(n - 1, x, 6 - x - y)
    sys.stdout.write('{} {}\n'.format(x,y))
    solution(n - 1, 6 - x - y, y)

n = int(sys.stdin.readline())
print(2**n-1)
solution(n, 1, 3)
