# baekjoon source = "https://www.acmicpc.net/problem/11651"
import sys

n = int(sys.stdin.readline())
result = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = sorted(result, key=lambda x: (x[1], x[0]))
for i in result:
    sys.stdout.write("{} {}\n".format(i[0], i[1]))
