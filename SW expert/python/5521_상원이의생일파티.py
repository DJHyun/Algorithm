import sys
sys.stdin = open("5521_상원이의생일파티.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    guest = []
    friend = []
    xx, yy = [], []
    for i in range(m):
        x, y = map(int, input().split())
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

    print(f'#{test_case} {len(guest) + len(friend)}')