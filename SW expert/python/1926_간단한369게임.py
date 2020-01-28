# SW Expert Academy
import sys

sys.stdin = open('input (14).txt', 'r')

check = ['3', '6', '9']
n = int(input())
for i in range(1, n + 1):
    cnt = 0
    for j in range(len(str(i))):
        if str(i)[j] in check:
            cnt += 1
    if cnt:
        print('-' * cnt, end=' ')
    else:
        print(i, end=' ')
