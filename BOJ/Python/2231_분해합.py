# baekjoon source = "https://www.acmicpc.net/problem/2231"
import sys

n = int(sys.stdin.readline().strip())

st = '1'
while int(st) < n:
    len_ = len(st)
    sum_ = 0
    for i in range(len_):
        sum_ += int(st[i])
    new_st = int(st)+sum_
    if new_st == n:
        print(st)
        break
    st = str(int(st)+1)
else:
    print(0)