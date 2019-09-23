# baekjoon source = "https://www.acmicpc.net/problem/1316"

import sys

T = sys.stdin.readline()
cnt = 0
for t in range(int(T)):
    list_compare = []
    s = list(sys.stdin.readline().strip())
    flag = True
    for i,st in enumerate(s):
        if st not in list_compare:
            list_compare.append(st)
        else:
            if s[i-1] != st:
                flag = False
                break
    if flag:
        cnt += 1
print(cnt)