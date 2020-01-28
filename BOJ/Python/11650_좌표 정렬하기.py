# baekjoon source = "https://www.acmicpc.net/problem/11650"
import sys

n = int(sys.stdin.readline())
result = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = sorted(result, key=lambda x: (x[0], x[1]))
for i in result:
    print(*i)
