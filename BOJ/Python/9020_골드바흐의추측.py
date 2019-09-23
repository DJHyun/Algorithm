# baekjoon source = "https://www.acmicpc.net/problem/1929"
import sys
import math

T = int(sys.stdin.readline())

for test_case in range(T):
    n = int(sys.stdin.readline())
    number = [1]*(n+1)
    number[0], number[1] = 0,0
    sq = int(math.sqrt(n))

    for i in range(2,sq+1):
        j = 2
        if number[i]:
            while i*j < (n+1):
                number[i*j] = 0
                j += 1

    for i in range((n+1)//2,-1,-1):
        if number[i]:
            if number[n-i]:
                print(i,n-i)
                break