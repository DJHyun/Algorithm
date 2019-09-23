# baekjoon source = "https://www.acmicpc.net/problem/1330"

import sys

a = list(map(int,sys.stdin.readline().split(" ")))

if a[0] > a[1]:
    print('>')
elif a[0] == a[1]:
    print('==')
else:
    print('<')