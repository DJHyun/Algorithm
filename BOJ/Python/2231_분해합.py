# baekjoon source = "https://www.acmicpc.net/problem/2231"
import sys
n = sys.stdin.readline().strip()
len_ = len(n)
for i in range(10 ** (len_-1), 10 ** len_ - 1):
    st = str(i)
    for j in range(len_):
        i += int(st[j])
    if i == int(n):
        print(int(st))
        break
