# baekjoon source = "https://www.acmicpc.net/problem/1967"

import sys
import itertools

n = int(sys.stdin.readline())
arr = [[] for _ in range(10001)]
mx = 0

print('asdf')
for i in range(n-1):
    print(i)
    a,b,c = map(int,sys.stdin.readline().split())
    arr[a].append([b,c])
    mx = b

print(mx)
it = itertools.combinations(range(1,10001),2)
for i in it:
    sys.stdout.write(str(i)+"\n")