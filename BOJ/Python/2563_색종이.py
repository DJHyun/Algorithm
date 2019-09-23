# baekjoon source = "https://www.acmicpc.net/problem/2563"
import sys
n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    x,y = map(int,sys.stdin.readline().split())
    for i in range(y,y+10):
        for j in range(x,x+10):
            if (j,i) not in arr:
                arr.append((j,i))

print(len(arr))