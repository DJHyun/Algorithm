# baekjoon source = "https://www.acmicpc.net/problem/1003"

import sys

def fibo(n):
    global zero, one

    if n == 0:
        return memo[0]

    if n == 1:
        return memo[1]

    if memo[n][0] or memo[n][1]:
        return memo[n]

    a = fibo(n-1)
    b = fibo(n-2)
    memo[n][0] = a[0] + b[0]
    memo[n][1] = a[1] + b[1]

    return memo[n]

T = int(sys.stdin.readline())

for test_case in range(T):
    num = int(sys.stdin.readline())
    memo = [[0,0] for _ in range(num+2)]
    memo[0] = [1,0]
    memo[1] = [0,1]

    if num > 1:
        fibo(num)
        print(memo[num][0], memo[num][1])
    else:
        print(memo[num][0], memo[num][1])


