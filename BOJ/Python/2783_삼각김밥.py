# baekjoon source = "https://www.acmicpc.net/problem/2783"

a = list(map(int, input().split()))
n = int(input())
other = [list(map(int, input().split())) for _ in range(n)]

result = 1000 / a[1] * a[0]

for i in range(n):
    result = min(result, 1000 / other[i][1] * other[i][0])

print('%0.2f' % result)
