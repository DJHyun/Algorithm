# baekjoon source = "https://www.acmicpc.net/problem/10886"
import sys

N = int(sys.stdin.readline())
z = 0
for i in range(N):
    z += 1 if int(sys.stdin.readline()) else -1
print("Junhee is cute!") if z > 0 else print("Junhee is not cute!")
