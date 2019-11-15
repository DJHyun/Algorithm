# baekjoon source = "https://www.acmicpc.net/problem/1063"

import sys

def check(x, y):
    if x < 0 or x > 7: return False
    if y < 0 or y > 7: return False
    return True

k, d, n = sys.stdin.readline().split()
k = list(k)
king = [int(k[1]) - 1, ord(k[0]) - 65]
dol = [int(d[1]) - 1, ord(d[0]) - 65]

for _ in range(int(n)):
    s = sys.stdin.readline().strip()
    x = king[0]
    y = king[1]
    if s == 'R':
        y += 1
        if check(x, y):
            if x == dol[0] and y == dol[1]:
                if check(dol[0], dol[1] + 1):
                    dol[1] += 1
                    king[1] += 1
            else:
                king[1] = y
    elif s == 'L':
        y -= 1
        if check(x, y):
            if x == dol[0] and y == dol[1]:
                if check(dol[0], dol[1] - 1):
                    dol[1] -= 1
                    king[1] -= 1
            else:
                king[1] = y
    elif s == 'B':
        x -= 1
        if check(x, y):
            if x == dol[0] and y == dol[1]:
                if check(dol[0] - 1, dol[1]):
                    dol[0] -= 1
                    king[0] -= 1
            else:
                king[0] = x
    elif s == 'T':
        x += 1
        if check(x, y):
            if x == dol[0] and y == dol[1]:
                if check(dol[0] + 1, dol[1]):
                    dol[0] += 1
                    king[0] += 1
            else:
                king[0] = x
    elif s == 'RT':
        y += 1
        x += 1
        if check(x, y):
            if x == dol[0] and y == dol[1]:
                if check(dol[0] + 1, dol[1] + 1):
                    dol[0] += 1
                    dol[1] += 1
                    king[0] += 1
                    king[1] += 1
            else:
                king[0] = x
                king[1] = y
    elif s == 'LT':
        y -= 1
        x += 1
        if check(x, y):
            if x == dol[0] and y == dol[1]:
                if check(dol[0] + 1, dol[1] - 1):
                    dol[0] += 1
                    dol[1] -= 1
                    king[0] += 1
                    king[1] -= 1
            else:
                king[0] = x
                king[1] = y
    elif s == 'RB':
        y += 1
        x -= 1
        if check(x, y):
            if x == dol[0] and y == dol[1]:
                if check(dol[0] - 1, dol[1] + 1):
                    dol[0] -= 1
                    dol[1] += 1
                    king[0] -= 1
                    king[1] += 1
            else:
                king[0] = x
                king[1] = y
    elif s == 'LB':
        y -= 1
        x -= 1
        if check(x, y):
            if x == dol[0] and y == dol[1]:
                if check(dol[0] - 1, dol[1] - 1):
                    dol[0] -= 1
                    dol[1] -= 1
                    king[0] -= 1
                    king[1] -= 1
            else:
                king[0] = x
                king[1] = y

print(chr(king[1] + 65), end='')
print(king[0] + 1)
print(chr(dol[1] + 65), end='')
print(dol[0] + 1)
