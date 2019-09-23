# baekjoon source = "https://www.acmicpc.net/problem/14888"
import itertools
'''
11
1 2 3 4 5 6 7 8 9 10 11
3 2 3 2

'''

n = int(input())
number = list(map(int, input().split()))
me = list(map(int, input().split()))
method = []
for i in range(len(me)):
    if me[i]:
        for j in range(me[i]):
            method.append((i + 1))

min_ = float('inf')
max_ = float('-inf')

it = itertools.permutations(method)
for i in it:
    idx = 0
    result = number[idx]
    for j in i:
        idx += 1
        if j == 1:
            result += number[idx]
        elif j == 2:
            result -= number[idx]
        elif j == 3:
            result *= number[idx]
        else:
            if result < 0:
                result = abs(result)//number[idx]
                result *= -1

            else:
                result //= number[idx]
    min_ = min(result, min_)
    max_ = max(result, max_)

print(max_)
print(min_)