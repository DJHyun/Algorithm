# baekjoon source = "https://www.acmicpc.net/problem/12851"
import sys

def solution(a):
    global result, cnt

    tq = []
    tq.append(a)
    index = 1
    while tq:
        q = tq[:]
        tq.clear()
        while q:
            t = q.pop(0)
            for i in range(3):
                if i == 2:
                    j = t * dx[i]
                    if j <= 100000:
                        if j == x:
                            result = index
                            cnt += 1
                        else:
                            if dp[j] >= index:
                                dp[j] = index
                                tq.append(j)
                else:
                    j = t + dx[i]
                    if 0 <= j <= 100000:
                        if j == x:
                            result = index
                            cnt += 1
                        else:
                            if dp[j] >= index:
                                dp[j] = index
                                tq.append(j)
        index += 1
        if result < index:
            return

n, x = map(int, sys.stdin.readline().split())
dp = [float('INF')] * 100001
dx = [-1, 1, 2]
result = float('INF')
cnt = 0
if n == x:
    result = 0
    cnt = 1
else:
    solution(n)
print(result)
print(cnt)
