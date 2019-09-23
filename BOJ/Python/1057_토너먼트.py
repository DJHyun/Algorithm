# baekjoon source = "https://www.acmicpc.net/problem/1057"
import sys

N, K, L = map(int, sys.stdin.readline().split())
check, result = 1, 0

if N == 1:
    print(-1)
else:
    while check:
        result += 1
        if N%2:
            for i in range(1,N+1,2):
                if (i == K and i+1 == L) or (i == L and i+1 == K):
                    check = 0
                    break
            else:
                N = N // 2 + 1
                K = K//2 + K%2
                L = L//2 + L%2
        else:
            for i in range(1,N+1,2):
                if (i == K and i+1 == L) or (i == L and i+1 == K):
                    check = 0
                    break
            else:
                N = N // 2
                K = K//2 + K%2
                L = L//2 + L%2

    print(result)

