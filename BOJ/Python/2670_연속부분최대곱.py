# baekjoon source = "https://www.acmicpc.net/problem/2670"

'''
8
1.1
0.7
1.3
0.9
1.4
0.8
0.7
1.4
'''
import sys
n = int(sys.stdin.readline())
result = 0
num = [float(sys.stdin.readline()) for _ in range(n)]
for i in range(n):
    check = 1
    for j in range(i,n):
        check *= num[j]
        result = max(result,check)
sys.stdout.write("%0.3f"%result)

