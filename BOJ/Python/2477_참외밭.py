# baekjoon source = "https://www.acmicpc.net/problem/2477"
'''
7
4 50
2 160
3 30
1 60
3 20
1 100

# 47600

7
4 50
2 100
3 20
1 70
3 30
1 30

# 20300

7
4 30
2 60
4 20
2 100
3 50
1 160

7
4 30
2 100
4 20
2 60
3 50
1 160
'''
import sys

T = int(sys.stdin.readline())
x,y,d = [],[],[]

for i in range(6):
    one, two = list(map(int,sys.stdin.readline().split()))
    if one == 1 or one == 2:
        x.append(two)
    else:
        y.append(two)
    d.append(one)

x_idx = x.index(max(x))
y_idx = y.index(max(y))

if (d.count(1) == 2 and d.count(3) ==2) or (d.count(2)==2 and d.count(4) == 2):
    x_two = x[(x_idx+1)%3]
    y_two = y[(y_idx-1)%3]
else:
    x_two = x[(x_idx-1)%3]
    y_two = y[(y_idx+1)%3]

sq = max(x)*max(y) - x_two*y_two
print(sq*T)
