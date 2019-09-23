# baekjoon source = "https://www.acmicpc.net/problem/2750"
'''
69
10
30
2
16
8
31
22
'''
import sys

n = int(sys.stdin.readline())
num = []

for i in range(n):
    num.append(int(sys.stdin.readline()))

for i in range(len(num)-1,0,-1):
    for j in range(0,i):
        if num[j] > num[j+1]:
            num[j],num[j+1] = num[j+1],num[j]

for i in num:
    print(i)

