import sys
import time
sys.stdin = open("3752_가능한시험점수.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # st = time.time()
    n = int(input())
    score = list(map(int, input().split()))
    new = [0]*10000
    visited = [0]*10000
    top = 0

    idx = 1
    for i in range(n):
        for j in range(idx):
            if not visited[new[j] + score[i]]:
                top += 1
                new[top] = new[j]+score[i]
                visited[new[j]+score[i]] = 1
                idx += 1


    print(f'#{test_case} {idx}')
    # print(time.time() - st)
