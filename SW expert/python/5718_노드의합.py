import sys
sys.stdin = open("노드의합.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int,input().split())
    result = [0]*(N+1)

    for i in range(M):
        d, v = map(int,input().split())
        result[d] = v

    for i in range(N,0,-1):
        if result[i] == 0:
            if i*2+1 > N:
                result[i] = result[i * 2]
            else:
                result[i] = result[i*2] + result[i*2+1]


    print('#{} {}'.format(test_case,result[L]))
