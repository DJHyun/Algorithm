import sys

sys.stdin = open("5247_연산.txt", "r")

T = int(input())

def bfs(x):
    global n, cnt
    tq = []
    tq.append(x)

    while tq:
        q = tq[:]
        tq.clear()
        while q:
            t = q.pop(0)
            visited[t] = 1
            for i in range(4):
                if i != 2:
                    if t + list_[i] <= 1000000 and not visited[t + list_[i]] and t + list_[i] > 0:
                        tq.append(t + list_[i])
                        visited[t + list_[i]] = 1
                else:
                    if t // 2 <= 1000000 and not visited[t // 2] and t % 2 == 0 and t // 2 > 0:
                        tq.append(t // 2)
                        visited[t // 2] = 1
                if n in tq:
                    return cnt
        cnt += 1

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    list_ = [1, -1, 2, 10]
    visited = [0] * 1000001
    cnt = 0
    bfs(m)
    print(f'#{test_case} {cnt+1}')
