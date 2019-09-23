# baekjoon source = "https://www.acmicpc.net/problem/2304"
import sys
n = int(sys.stdin.readline())

arr = [0] * 1001
max_ = index = end = 0
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split(" "))
    arr[a] = b
    if max_ < b:
        max_ = b
        index = a
    end = max(end, a)

result = max_
check = arr[0]
check_index = 0
for i in range(index):
    if check < arr[i]:
        result += check * (i - check_index)
        check = arr[i]
        check_index = i
result += check * (index - check_index)

check = arr[end]
check_index = end
for i in range(end, index, -1):
    if check < arr[i]:
        result += check * (check_index - i)
        check = arr[i]
        check_index = i
result += check * (check_index - index)

print(result)
