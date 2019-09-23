# SW Expert Academy
import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    a, b, x, y = map(int, input().split())
    result = 0
    m = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    if a == x:
        result += (y - b) + 1

    else:

        result += m[a]-b+1
        result += y
        month = []
        for i in range(a + 1, x):
            month.append(i)
        for i in month:
            result += m[i]

    print(f'#{test_case} {result}')
