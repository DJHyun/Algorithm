# baekjoon source = "https://www.acmicpc.net/problem/1978"
import sys

N = int(sys.stdin.readline())
number = list(map(int,sys.stdin.readline().split()))
cnt = 0 

for i in number:
    if i != 1 and i != 4:
        for num in range(2,i//2):
            if i%num == 0:
                break
        else:
            print(i)
            cnt += 1

print(cnt)