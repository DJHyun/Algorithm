# baekjoon source = "https://www.acmicpc.net/problem/2635"

import sys

def solution(a,b):
    if b < 0:
        return result
    result.append(str(b))
    return solution(b,a-b)


N = int(sys.stdin.readline())
max_ = 0
an = []
for i in range(1,30000):
    result = [str(N)]
    solution(N,i)
    if max_ < len(result):
        max_ = len(result)
        an = result[:]

print(max_)
print(' '.join(an))

