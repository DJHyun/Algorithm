import sys
sys.stdin = open("Contact.txt", "r")

def bfs(matrix,start):
    tq = []

    tq.append(start)
    visited[start] = 1

    while tq:
        q = tq[:]
        tq = []
        result.append(q[:])
        while q:
            t = q.pop(0)
            for i in range(len(matrix[t])):
                if matrix[t][i] == 1 and not visited[i]:
                    tq.append(i)
                    visited[i] = 1

for test_case in range(1, 11):
    len_, start = map(int,input().split())
    node = list(map(int,input().split()))
    matrix = [[0]*(max(node)+1) for _ in range(max(node)+1)]
    visited = [0]*(max(node)+1)
    result = []

    for i in range(0,len_,2):
        matrix[node[i]][node[i+1]] = 1

    bfs(matrix,start)

    print(f'#{test_case} {max(result[len(result)-1])}')