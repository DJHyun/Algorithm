# baekjoon source = "https://www.acmicpc.net/problem/5597"
import sys

check = list(range(1,31))
for _ in range(28):
    student = int(sys.stdin.readline())
    if student in check:
        check.pop(check.index(student))

print(check[0])
print(check[1])
