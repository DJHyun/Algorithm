# baekjoon source = "https://www.acmicpc.net/problem/1038"

import sys

N = int(sys.stdin.readline())
number = list(range(10))
nums = []

for i in range(1,(1 << len(number))):
    check = []
    for j in range(len(number)):
        if i & (1 << j):
            check.append(str(j))
    nums.append(int(''.join(check[::-1])))

nums.sort()

if N >= 1023:
    print(-1)
else:
    print(nums[N])