# baekjoon source = "https://www.acmicpc.net/problem/2309"
import sys

num = [0]*9
result = 0
flag = True

for i in range(9):
    num[i] = int(sys.stdin.readline())

num = sorted(num)

for i in range(9):
    if flag:
        for j in range(i+1,9):
            result = 0
            for n in range(9):
                if n != i and n != j:
                    result += num[n]

            if result == 100:
                result = (i,j)
                flag = False
                break
    else:
        break

for i in range(9):
    if i not in result:
        print(num[i])