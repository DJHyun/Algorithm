import sys

sys.stdin = open("2805_농작물수확하기.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int,list(input()))) for _ in range(N)]
    result = 0

    for i in range(N):
        ra = N//2
        sm = abs(ra-i)
        if ra >= i:
            la = ra + i
        else:
            a = N-i-1
            la = ra+(a%ra)
        for j in range(sm,la+1):
            result += arr[i][j]

    print('#{} {}'.format(test_case,result))

