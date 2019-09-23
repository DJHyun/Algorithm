# baekjoon source = "https://www.acmicpc.net/problem/2581"
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
sum_,min_ = 0,0
for i in range(M,N-1,-1):
    if i != 1 and i != 4:
        for j in range(2,i//2):
            if i%j == 0:
                break
        else:
            sum_ += i
            min_ = i

if sum_ == 0:
    print(-1)
else:
    print(sum_)
    print(min_)

