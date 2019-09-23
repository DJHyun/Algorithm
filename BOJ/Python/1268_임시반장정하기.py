# baekjoon source = "https://www.acmicpc.net/problem/1193"
import sys

T = int(sys.stdin.readline())
grade,check = [[0]*T for _ in range(5)],[[0]*T for _ in range(T)]
max_,result = 0,0

for j in range(T):
    a = list(map(int,sys.stdin.readline().split()))
    for i in range(5):
        grade[i][j] = a[i]

for i in range(5):
    for j in range(T):
        for a in range(j+1,T):
            if grade[i][j] == grade[i][a]:
                    check[j][a] = 1
                    check[a][j] = 1
    
for i in range(T):
    if max_ < check[i].count(1):
        max_ = check[i].count(1)
        result = i

print(result+1)