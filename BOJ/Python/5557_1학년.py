# baekjoon source = "https://www.acmicpc.net/problem/5557"

import sys

def solution(depth,s):
    global result,n

    if s < 0 or s > 20:
        return

    if depth == n-2:
        if s == score[n-1]:
            result += 1
        return 1



    if memo[depth][s]:
        return memo[depth][s]

    memo[depth][s] = s
    solution(depth+1,s+score[depth+1])
    solution(depth+1,s-score[depth+1])


n = int(sys.stdin.readline())
score = list(map(int,sys.stdin.readline().split()))
result = 0
memo = [[0]*21 for _ in range(n-2)]


solution(0,score[0])
print(result)