# baekjoon source = "https://www.acmicpc.net/problem/5596"
import sys
a = sum(list(map(int,sys.stdin.readline().split())))
b = sum(list(map(int,sys.stdin.readline().split())))
print(a if a >= b else b)

