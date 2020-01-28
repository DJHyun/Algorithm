# SW Expert Academy
import sys
sys.stdin = open("파리퇴치.txt","r")
T = int(input())
for test_case in range(1, T +1 ):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    cnt,max_ = 0,0
    for i in range(N-M+1):
        for j in range(N-M+1):
            cnt = 0
            for a in range(M):
                for b in range(M):
                    cnt += arr[i+a][j+b]
            max_ = max(max_,cnt)

    print('#{} {}'.format(test_case,max_))


