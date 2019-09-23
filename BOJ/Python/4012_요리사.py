import sys
import itertools

sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    it = list(itertools.combinations(range(n), n//2))
    len_ = len(it)
    sum_ = [0]*len_
    result = float('inf')

    for i,v in enumerate(it):
        for j in list(itertools.combinations(v,2)):
            sum_[i] += arr[j[0]][j[1]]
            sum_[i] += arr[j[1]][j[0]]

    for i in range(len_):
        result = min(result, abs(sum_[i]-sum_[len_-1-i]))

    print(f'#{test_case} {result}')
