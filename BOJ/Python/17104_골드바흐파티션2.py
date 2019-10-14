# baekjoon source = "https://www.acmicpc.net/problem/17104"
'''
5
6
8
10
12
100

7
1000000
1000000
1000000
1000000
1000000
1000000
1000000
'''
import sys
arr = [0] * 1000001
for i in range(2, 1000001):
    if arr[i] == -1:
        continue
    arr[i] = 1
    index = 2
    while i * index <= 1000000:
        arr[i * index] = -1
        index += 1

t = int(sys.stdin.readline())
for _ in range(t):
    number = int(sys.stdin.readline())
    result = 0
    for i in range(number // 2 + 1):
        if arr[i] == 1 and arr[number - i] == 1:
            result += 1
    sys.stdout.write(str(result)+"\n")
