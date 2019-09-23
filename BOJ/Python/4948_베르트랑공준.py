# baekjoon source = "https://www.acmicpc.net/problem/1929"
import sys
import math

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    list_ = [1]*(2*n+1)
    list_[0],list_[1],cnt = 0,0,0
    sq = int(math.sqrt(2*n))
    
    for i in range(2,sq+1):
        j = 2
        if list_[i]:
            while i*j <(2*n+1):
                list_[i*j] = 0
                j += 1
    
    for i in range(n+1,2*n+1):
        if list_[i]:
            cnt += 1

    print(cnt)