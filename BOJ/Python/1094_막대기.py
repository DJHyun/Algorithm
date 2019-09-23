# baekjoon source = "https://www.acmicpc.net/problem/1094"
import sys

a, top = [0] * 10, 0
a[0] = 64
x = int(sys.stdin.readline())

while sum(a) != x:
    a[top] = a[top]//2
    top += 1
    a[top] = a[top-1]
    if sum(a[:top]) >= x:
        a[top] = 0
        top -= 1
        
print(top+1)

        