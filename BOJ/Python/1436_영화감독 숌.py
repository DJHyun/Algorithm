# baekjoon source = "https://www.acmicpc.net/problem/1436"

import sys

n = int(sys.stdin.readline())

if n == 1:
    sys.stdout.write('666')
else:
    start = 1666
    index = 2
    while index < n:
        start += 1
        s = str(start)
        if '666' in s:
            index += 1
    sys.stdout.write(str(start))
