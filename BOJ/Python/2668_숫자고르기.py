# baekjoon source = "https://www.acmicpc.net/problem/2668"

'''
7
3
1
1
5
5
4
6
'''
import sys

n = int(sys.stdin.readline())
first = [i for i in range(1, n + 1)]
second = [int(sys.stdin.readline()) for _ in range(n)]

while True:
    first_len = len(first)
    second_len = len(second)
    first_index = 0

    while first_index < len(first):
        if first[first_index] not in second:
            first.pop(first_index)
            second.pop(first_index)
        else:
            first_index += 1

    second_index = 0
    while second_index < len(second):
        if second[second_index] not in first:
            first.pop(second_index)
            second.pop(second_index)
        else:
            second_index += 1
    if first_len == len(first) and second_len == len(second):
        break

sys.stdout.write(str(len(first)) + "\n")
for a in first:
    sys.stdout.write(str(a) + "\n")
