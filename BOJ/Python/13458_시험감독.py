# baekjoon source = "https://www.acmicpc.net/problem/13458"
import math
import sys
n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
b,c = map(int,sys.stdin.readline().split())
result = n

for i in range(n):
    if math.ceil(arr[i]-b/c) > 0:
        result += math.ceil(arr[i]-b/c)

print(result)




