# baekjoon source = "https://www.acmicpc.net/problem/1065"

import sys

N = int(sys.stdin.readline())
result = 0

for i in range(1,N+1):
    if(len(str(i)) <= 2):
        result += 1
    else:
        str_num = list(map(int,str(i)))
        if ((str_num[0]-str_num[1]) == (str_num[1]-str_num[2])):
            result += 1

print(result)