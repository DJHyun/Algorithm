import sys
sys.stdin = open("2070_큰놈,작은놈,같은놈.txt","r")

T = int(input())
for test_case in range(1, T + 1):
    a,b = map(int,input().split())
    if a > b:
        print(f'#{test_case} {">"}')
    elif a < b:
        print(f'#{test_case} {"<"}')
    else:
        print(f'#{test_case} {"="}')