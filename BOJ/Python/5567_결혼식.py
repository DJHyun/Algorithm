# baekjoon source = "https://www.acmicpc.net/problem/5567"
import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

guest = []
friend = []
xx, yy = [], []
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    if x == 1:
        friend.append(y)
    else:
        xx.append(x)
        yy.append(y)
if xx:
    for i in range(len(xx)):
        if xx[i] in friend and yy[i] not in guest and yy[i] not in friend:
            guest.append(yy[i])

        if yy[i] in friend and xx[i] not in guest and xx[i] not in friend:
            guest.append(xx[i])

print(len(guest) + len(friend))
