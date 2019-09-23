# baekjoon source = "https://www.acmicpc.net/problem/2455"
import sys

result,max_ = 0,-1
for test_case in range(4):
    o, i = map(int,sys.stdin.readline().split())
    if test_case == 0:
        result = i
    elif test_case == 3:
        result -= o
    else:
        result = result - o + i

    if max_ < result:
        max_ = result

print(max_)