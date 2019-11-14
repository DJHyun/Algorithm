# baekjoon source = "https://www.acmicpc.net/problem/1120"

import sys

a,b = sys.stdin.readline().split()
len_a = len(a)
m = len(b)-len_a

result = float('inf')
for i in range(m+1):
    count = 0
    for j in range(i,i+len_a):
        if a[j-i] != b[j]:
            count += 1

    result = min(result,count)

print(result)
