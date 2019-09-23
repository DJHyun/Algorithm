# SW Expert Academy
import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1, T + 1):
    t = int(input())
    score = list(map(int,input().split()))
    result = {}

    for i in score:
        if i not in result:
            result[i] = 1
        else:
            result[i] += 1
    result = sorted(result, key=lambda x: (result[x],x), reverse=True)
    print(f'#{test_case} {result[0]}')