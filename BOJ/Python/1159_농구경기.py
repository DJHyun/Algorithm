# baekjoon source = "https://www.acmicpc.net/problem/1159"

import sys

check = {}
N = int(sys.stdin.readline())

for i in range(N):
    name = sys.stdin.readline()

    if name[0] in check:
        check[name[0]] += 1
    else:
        check[name[0]] = 1

result = []
for i,v in check.items():
    if v >= 5:
        result.append(i)
result.sort()


if result:
    print(''.join(result))
else:
    print('PREDAJA')