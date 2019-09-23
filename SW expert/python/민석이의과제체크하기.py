import sys
sys.stdin = open("민석이의과제체크하기.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    li = list(map(int,input().split()))
    N,M = list(range(1,li[0]+1)),li[1]
    hu = list(map(int,input().split()))
    result = ''
    for i in hu:
        for j in range(len(N)):
            if i == N[j]:
                N[j] = 0
                break
    for i in N:
        if i != 0:
            result += str(i) + ' '

    print(f'#{test_case} {result}')

    