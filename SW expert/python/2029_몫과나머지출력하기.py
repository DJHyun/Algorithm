import sys
sys.stdin = open("2029_몫과나머지출력하기.txt","r")

T = int(input())
for test_case in range(1, T + 1):
    a,b = map(int,input().split())

    print(f'#{test_case} {a//b} {a%b}')