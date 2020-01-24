# SW Expert Academy
import sys

sys.stdin = open('input (23).txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    money = int(input())
    result = 0
    gold = 50000
    flag = True

    print(f'#{test_case}')
    while gold != 5:
        if money >= gold:
            cnt = money // gold
            money -= gold * cnt
            print(cnt,end=' ')
        else:
            print(0, end=' ')
        if flag:
            gold //= 5
            flag = False
        else:
            gold //= 2
            flag = True

    print()

