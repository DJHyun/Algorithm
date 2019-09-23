# baekjoon source = "https://www.acmicpc.net/problem/2559"
'''
10 2
3 -2 -4 -9 0 3 7 13 8 -3

10 5
3 -2 -4 -9 0 3 7 13 8 -3

5 3
5 5 5 2 1000

100000 5
'''
import sys

N, K = map(int,sys.stdin.readline().split())
num = list(map(int,sys.stdin.readline().split()))

max_ = 0; sum_ = 0
for i in range(K):
    sum_ += num[i]
    max_ = sum_

for i in range(K,N):
    sum_ -= num[i-K]
    sum_ += num[i]
    max_ = max(max_,sum_)

print(max_)





# import sys
# import time

# st = time.time()

# N, K = map(int,sys.stdin.readline().split())
# # num = list(map(int,sys.stdin.readline().split()))
# num = list(range(N))
# numbers = result = 0

# for i in range(N-K+1):
#     numbers += sum(num[i:i+K])
#     result = max(result,numbers)
#     numbers = 0

# print(result)

# print((time.time() - st))