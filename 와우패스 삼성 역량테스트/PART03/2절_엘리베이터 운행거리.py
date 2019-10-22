'''
3
-2 10
1 15
7 -1
'''

t = int(input())
result = 1
score = 0
for tc in range(t):
    a, b = map(int, input().split())
    for i in range(2):
        if i == 0:
            if result - a < 0:
                score += abs(result - a) + 1
            else:
                score += abs(result - a)
        else:
            if result - b < 0:
                score += abs(result - b) + 1
            else:
                score += abs(result - b)
    result = b

print(score)
