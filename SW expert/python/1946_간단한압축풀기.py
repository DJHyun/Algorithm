# SW Expert Academy
import sys
sys.stdin = open('1946_간단한압축풀기.txt','r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    result = ''

    for i in range(N):
        st, num = input().split()
        result += st * int(num)

    print('#{}'.format(test_case))
    idx = 1
    for i in range(len(result)):
        if idx == 10:
            print(result[i])
            idx = 0
        else:
            print(result[i],end='')
        idx += 1
    print()