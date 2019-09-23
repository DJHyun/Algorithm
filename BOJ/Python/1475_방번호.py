# baekjoon source = "https://www.acmicpc.net/problem/1475"
import sys
import math

N = list(sys.stdin.readline().strip())
dict_ = {}

for i in range(len(N)):
    if N[i] == '9':
        N[i] = '6'        

for i in N:
    if i not in dict_:
        dict_[i] = 1
    else:
        dict_[i] += 1

if '6' in N:
    dict_['6'] = math.ceil(dict_['6']/2)

print(max(dict_.values()))