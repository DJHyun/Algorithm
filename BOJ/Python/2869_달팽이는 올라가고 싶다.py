# baekjoon source = "https://www.acmicpc.net/problem/2869"

import sys

a, b, v = map(int, sys.stdin.readline().split())
left = 1
right = v
mid = (right+left)//2

while True:

    print(left,mid,right)
    if (a-b)*mid+a > v:
        right = mid -1
    else:
        left = mid + 1

    if left >= right:
        print(mid)
        break

    mid = (right+left)//2


