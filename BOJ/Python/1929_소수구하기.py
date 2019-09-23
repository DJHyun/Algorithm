# baekjoon source = "https://www.acmicpc.net/problem/1929"
import sys
import math

M,N = map(int,sys.stdin.readline().split())
list_ = [1] * (N+1) 
list_[0],list_[1] = 0,0
N = int(math.sqrt(N))

for i in range(2,N+1):
    if list_[i]:
        j = 2
        while i*j < len(list_):
            list_[i*j] = 0
            j += 1

for i in range(M,len(list_)):
    if list_[i]:
        print(i)
