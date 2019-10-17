# baekjoon source = "https://www.acmicpc.net/problem/16673"

'''
9
3+8*7-9*2

19
1*2+3*4*5-6*7*8*9*0

5
1-3-7
'''
import sys
import itertools

def cal(x):
    result = int(x[0])
    for i in range(1, n, 2):
        if x[i] == float('inf'):
            continue
        if x[i] == '+':
            result += int(x[i + 1])
        elif x[i] == '-':
            result -= int(x[i + 1])
        elif x[i] == '*':
            result *= int(x[i + 1])

    return result

n = int(sys.stdin.readline())
arr = list(sys.stdin.readline().strip())
count = n // 4
if n % 4 == 3:
    count += 1
start = cal(arr)
check = []

for i in range(0, n - 2, 2):
    check.append([i, i + 2])

for i in range(1, count + 1):
    it = itertools.combinations(check, i)
    it = list(it)
    for ad in it:
        check_ad = []
        for a in ad:
            check_ad += a
        check_number = i * 2
        if len(set(check_ad)) != check_number:
            continue
        new_arr = [float('-inf')] * n
        for c in ad:
            if arr[c[0] + 1] == '+':
                score = int(arr[c[0]]) + int(arr[c[1]])
            elif arr[c[0] + 1] == '-':
                score = int(arr[c[0]]) - int(arr[c[1]])
            elif arr[c[0] + 1] == '*':
                score = int(arr[c[0]]) * int(arr[c[1]])

            new_arr[c[0]] = score

            for ma in range(n):
                if ma == c[1] or ma == c[0]+1:
                    new_arr[ma] = float('inf')
                if new_arr[ma] == float('-inf'):
                    new_arr[ma] = arr[ma]
        st = cal(new_arr)
        start = max(st,start)

print(start)
