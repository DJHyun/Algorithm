# baekjoon source = "https://www.acmicpc.net/problem/11650"

import sys

n = int(sys.stdin.readline())
result = [list(map(int,sys.stdin.readline().split()))]
for i in range(n-1):
    ne = list(map(int,sys.stdin.readline().split()))
    for j in range(i+1):
        if ne[0] > result[j][0]:
            continue
        elif ne[0] == result[j][0]:
            if ne[1] < result[j][1]:
                result.insert(j,ne)
                break
        else:
            result.insert(j,ne)
            break
    else:
        result.append(ne)
for i in result:
    print(*i)