# baekjoon source = "https://www.acmicpc.net/problem/2116"
'''
5
2 3 1 6 5 4
3 1 2 4 6 5
5 6 4 1 3 2
1 3 6 2 4 5
4 1 6 5 2 3
'''
import sys

def check_fun(a):
    check = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
    return check[a]

T = int(sys.stdin.readline())
num = [0] * T
sum_num = [[0] * 4 for _ in range(T)]
a = [0] * T
for i in range(T):
    num[i] = list(map(int, sys.stdin.readline().split()))

max_ = 0
for i in range(6):
    result = 0
    first = i
    last = check_fun(first)
    max_number = list(range(1, 7))
    max_number.remove(num[0][first])
    max_number.remove(num[0][last])
    result += max(max_number)
    for j in range(T - 1):
        last = num[j + 1].index(num[j][first])
        first = check_fun(last)
        max_number = list(range(1, 7))
        max_number.remove(num[j + 1][last])
        max_number.remove(num[j + 1][first])
        result += max(max_number)
    max_ = max(max_,result)

print(max_)
