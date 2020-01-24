# baekjoon source = "https://www.acmicpc.net/problem/1085"
import sys
x, y, w, h = map(int, sys.stdin.readline().split())
print(min(abs(x - 0), abs(y - 0), w - x, h - y))