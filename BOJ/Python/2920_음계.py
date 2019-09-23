# baekjoon source = "https://www.acmicpc.net/problem/8958"

numbers = list(map(int,input().split()))
result = 'mixed'
if numbers[0] == 1:
    li = list(range(1,9))
    if numbers == li:
        result = 'ascending'
elif numbers[0] == 8:
    li = list(range(8,0,-1))
    if numbers == li:
        result = 'descending'
print(result)