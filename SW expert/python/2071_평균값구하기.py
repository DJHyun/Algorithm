import sys
sys.stdin = open("2071_평균값구하기.txt","r")

T = int(input())
for test_case in range(1, T + 1):
    numbers = list(map(int,input().split()))


    print(f'#{test_case} {round(sum(numbers)/10)}')