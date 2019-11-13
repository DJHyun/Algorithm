# baekjoon source = "https://www.acmicpc.net/problem/17845"
'''
110 3
650 40
700 60
60 40
'''
import sys

def solution(pos, cap):
    print(pos,cap)
    if pos == k:
        return
    ret = memo[pos][cap]
    if ret != -1:
        print(ret)
    if sub[pos][1] <= cap:
        ret = solution(pos+1,cap-sub[pos][0])+sub[pos][0]
    ret = max(ret,solution(pos+1,cap))
    memo[pos][cap] = ret
    print(ret)
    return memo[pos][cap]

n, k = map(int, sys.stdin.readline().split())
memo = [[-1]*(n+1) for _ in range(k)]
for i in memo:
    print(i)
sub = [list(map(int,sys.stdin.readline().split())) for _ in range(k)]

solution(0,n)