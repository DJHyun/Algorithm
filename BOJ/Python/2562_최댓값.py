# baekjoon source = "https://www.acmicpc.net/problem/2562"

index, max = 0,0

for i in range(9):
    n = int(input())
    if n > max:
        max = n
        index = i+1

print(max)
print(index)