# baekjoon source = "https://www.acmicpc.net/problem/10539"

n = int(input())
number = list(map(int, input().split()))

result = [0] * n
idx = 0
result[0] = number[0]
for i in range(1, n):
    idx += 1
    result[idx] = number[i] * (i + 1) - sum(result[:idx])

print(' '.join(list(map(str,result))))
