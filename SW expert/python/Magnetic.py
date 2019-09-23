import sys
sys.stdin = open("Magnetic.txt", "r")

for test_case in range(1, 11):
    T = int(input())
    number = [[0]*T for _ in range(T)]
    for i in range(T):
        number[i] = list(map(int,input().split()))
    cnt = [0] * T

    for i in range(T):
        for j in range(T):
            if number[i][j] == 1:
                if i < 99:
                    if number[i+1][j] == 0:
                        number[i][j], number[i+1][j] = number[i+1][j],number[i][j]
                else:
                    number[i][j] = 0

    for i in range(T):
        for j in range(T-1):
            if number[j][i] == 1:
                if number[j+1][i] == 2:
                    cnt[i] += 1
    
    print(f'#{test_case} {sum(cnt)}')