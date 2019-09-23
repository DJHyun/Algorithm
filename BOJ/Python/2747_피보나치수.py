# baekjoon source = "https://www.acmicpc.net/problem/2747"
import sys
one, two = 0, 1

for i in range(2, int(sys.stdin.readline()) + 1):
    if i % 2:
        two += one
    else:
        one += two

print(max(one, two))