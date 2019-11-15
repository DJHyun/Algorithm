# baekjoon source = "https://www.acmicpc.net/problem/1062"

import sys
import itertools

n, k = map(int, sys.stdin.readline().split())
if k < 5:
    print(0)
else:
    check = ['a','n','t','i','c']
    go = []
    for i in range(98,123):
        if chr(i) not in check:
            go.append(chr(i))

    cnt = k-5
    it = itertools.combinations(go,cnt)
    arr = []

    c = 0
    for i in range(n):
        s = sys.stdin.readline().strip()
        ne = ''
        for j in s:
            if j not in check:
                ne += j
        arr.append(ne)
        if len(ne) <= cnt:
            c += 1
    result = 0
    for i in it:
        cnt = 0
        for j in arr:
            for x in j:
                if x not in check and x not in i:
                    break
            else:
                cnt += 1
        if cnt == c:
            print(c)
            break
        result = max(result,cnt)
    else:
        print(result)