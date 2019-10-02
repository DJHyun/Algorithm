# baekjoon source = "https://www.acmicpc.net/problem/2670"

import sys
n = int(sys.stdin.readline())
max_ = 0
result = 1
num = [0]*n
for i in range(n):
    number = float(sys.stdin.readline())
    max_ = max(max_,number)
    result *= number
    num[i] = number

print(max_)
for i in range(n):
    check = result
    check /= num[i]
    
print(result)