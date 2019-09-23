# baekjoon source = "https://www.acmicpc.net/problem/2804"

'''
BANANA PIDZAMA
'''
input_ = list(input().split())
a, b = list(input_[0]), list(input_[1])
arr = [['.'] * len(a) for _ in range(len(b))]
sero, garo = -1, -1
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            sero = j
            garo = i
            break
    if sero != -1:
        break

for i in range(len(a)):
    arr[sero][i] = a[i]
for j in range(len(b)):
    arr[j][garo] = b[j]

for i in arr:
    print(''.join(i))
