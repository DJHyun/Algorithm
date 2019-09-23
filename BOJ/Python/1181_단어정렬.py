# baekjoon source = "https://www.acmicpc.net/problem/1157"

import sys

N = int(sys.stdin.readline())
my_dict = {}

for test_case in range(N):
    my_str = sys.stdin.readline().strip()
    if my_str not in my_dict:
        my_dict[my_str] = len(my_str)

my_dict = sorted(my_dict.items(), key=lambda a : (a[1], a[0]))

for i in my_dict:
    print(i[0])