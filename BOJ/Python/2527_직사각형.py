# baekjoon source = "https://www.acmicpc.net/problem/2527"
'''
3 10 50 60 100 100 200 300
45 50 600 600 400 450 500 543
11 120 120 230 50 40 60 440
35 56 67 90 67 80 500 600

35 56 67 90 67 100 500 600
10 10 20 20 15 15 16 16
1 1 5 5 5 5 10 10
1 1 5 5 5 3 10 10

1 1 2 2 0 0 1 1
1 1 5 5 10 10 11 11
10 10 11 11 1 1 5 5
1 1 5 5 4 5 10 10

4 3 10 20 1 1 4 3
5 9 20 30 20 30 100 100
5 9 20 20 5 9 20 20

1 1 3 3 3 4 7 9
1 1 4 3 3 3 7 9
1 1 3 3 3 4 7 9
1 1 4 3 3 3 7 9
'''
import sys

for test_case in range(1, 5):
    x, y, p, q, a, b, c, d = list(map(int, sys.stdin.readline().split()))
    print(x, y, p, q, a, b, c, d)

    if x > c or y > d or a > p or b > q:
        print('d')
    elif (x == c and y == d) or (x == c and q == b) or (p == a and y == d) or (p == a and q == b):
        print('c')
    elif x == c or y == d or a == p or b == q:
        print('b')
    else:
        print('a')
