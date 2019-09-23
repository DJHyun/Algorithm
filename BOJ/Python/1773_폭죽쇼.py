# baekjoon source = "https://www.acmicpc.net/problem/1773"
n, c = map(int, input().split())
fire = [int(input()) for _ in range(n)]
result = 0

for i in range(1,c+1):
    for j in range(n):
        if not i%fire[j]:
            result += 1
            break

print(result)