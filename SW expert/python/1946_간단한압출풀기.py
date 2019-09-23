# SW Expert Academy
import sys
sys.stdin = open('input (5).txt','r')

T = int(input())
for test_case in range(1, T + 1):
    print(f'#{test_case}')
    n = int(input())
    st = ''
    for _ in range(n):
        a,b = input().split()
        st += a*int(b)

    for i,v in enumerate(st):

        if i != 0 and i%10 == 0:
            print()
            print(v,end='')
        else:
            print(v,end='')

    print()