# SW Expert Academy
import sys

sys.stdin = open('input (6).txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    a = b = c = d = e = 0
    number = [2,3,5,7,11]

    result = [0]*5

    idx = 0
    while number[idx] <= n:
        if not n%number[idx]:
            n //= number[idx]
            result[idx] += 1
        else:
            idx += 1


    print(f'#{test_case} {" ".join(map(str,result))}')
