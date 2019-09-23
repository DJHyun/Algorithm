# baekjoon source = "https://www.acmicpc.net/problem/14500"



n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [[0], [1]]
dy = [[1], [0]]
print(n, m)
for i in arr:
    print(i)

result = 0
for i in range(n):
    sum_ = 0
    for j in range(m - 3):
        sum_ = sum(arr[i][j:j + 4])
    result = max(result, sum_)

for i in range(m):
    for j in range(n-3):
        sum_ = 0
        for z in range(4):
            sum_ += arr[j+z][i]
        result = max(result, sum_)

for i in range(n-1):
    for j in range(m-1):
        sum_ = 0
        for a in range(2):
            for b in range(2):
                print(i+a,b+j)
                sum_ += arr[i+a][j+b]
        result = max(result, sum_)

print(result)


print(result)
