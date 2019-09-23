import sys
sys.stdin = open("2072_홀수만더하기.txt","r")

T = int(input())
for test_case in range(1, T + 1):
    numbers = list(map(int,input().split()))
    result = 0

    for i in numbers:
        if i%2:
            result += i

    print(f'#{test_case} {result}')