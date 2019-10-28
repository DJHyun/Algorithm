# baekjoon source = "https://www.acmicpc.net/problem/2644"
import sys

n = int(sys.stdin.readline())
a,b = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())
arr = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    x,y = map(int,sys.stdin.readline().split())
    arr[x][y] = 1
    arr[y][x] = 1

for i in arr:
    print(i)