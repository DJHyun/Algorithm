# baekjoon source = "https://www.acmicpc.net/problem/6603"

import sys
import itertools

while True:
    numbers = list(map(int, sys.stdin.readline().split()))
    if numbers[0] == 0:
        break
    for i in itertools.combinations(numbers[1:],6):
        print(' '.join(map(str,i)))
    print()