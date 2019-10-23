'''
3
-2 10
1 15
7 -1
'''

t = int(input())
start = 1
result = 0
for tc in range(1, t + 1):
    a, b = map(int, input().split())
    if a < 0:
        a += 1
    if b < 0:
        b += 1
    result += abs(start - a)
    start = a
    result += abs(start - b)
    start = b

print(result)
