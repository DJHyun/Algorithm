# baekjoon source = "https://www.acmicpc.net/problem/3088"
import sys

'''
5
3 4 1
2 5 6
7 2 8
2 1 9
11 10 9
'''

n = int(sys.stdin.readline())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
memo = [0]*(n+1)

for i in range(n):
    for j in range(i+1,n):
        for z in range(3):
            if arr[j][z] in arr[i]:


print(memo)