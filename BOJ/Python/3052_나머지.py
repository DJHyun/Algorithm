# baekjoon source = "https://www.acmicpc.net/problem/3052"

result = set()

for i in range(10):
    n = int(input())
    n %= 42
    result.add(n)

print(len(result))