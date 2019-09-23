# baekjoon source = "https://www.acmicpc.net/problem/4153"

a = list(map(int,input().split()))
while sum(a) != 0:
    a.sort()

    if a[0]**2 + a[1]**2 == a[2] ** 2:
        print('right')
    else:
        print('wrong')

    a = list(map(int,input().split()))

