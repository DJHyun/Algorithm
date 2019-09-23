import sys

sys.stdin = open("5186_이진수2.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = float(input())
    result = []
    while N != int(N):
        N = N * 2
        result.append(str(int(N)))
        N -= int(N)

    if len(result) <= 12:
        print(f'#{test_case} {"".join(result)}')
    else:
        print(f'#{test_case} overflow')
