# baekjoon source = "https://www.acmicpc.net/problem/3053"
import sys
import math

r = int(sys.stdin.readline())
print("%0.6f" % float(r**2*(math.atan(1)*4)))
print("%0.6f" % float(2*r**2))