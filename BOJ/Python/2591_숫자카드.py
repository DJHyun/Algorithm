# baekjoon source = "https://www.acmicpc.net/problem/2591"

import sys

def solution(x,depth,c):
    global result

    print(x,depth,c)
    if x > len(memo) -1:
        print(x)
        return

    if depth == c:
        print(x)
        result +=1
        return

    for i in range(x,len(memo)):
        if memo[i]:
            solution(i+2,depth+1,c)

n = list(sys.stdin.readline().strip())
len_ = len(n)
result = 1
count = len_//2
memo = [0]*(len_-1)

for i in range(len_-1):
    if int(n[i] + n[i+1]) <= 34:
        memo[i] = 1

print(memo)

for i in range(1,count+1):
    for j in range(len(memo)):
        solution(j,0,i)


print(n)
print(result)