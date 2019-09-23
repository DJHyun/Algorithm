# baekjoon source = "https://www.acmicpc.net/problem/10798"
import sys

arr = [0] * 5
max_ = 0
for i in range(5):
    arr[i] = list(sys.stdin.readline().strip())
    max_ = max(max_, len(arr[i]))

for i in range(max_):
    for j in range(5):
        try:
            print(arr[j][i], end='')
        except:
            pass
