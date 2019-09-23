import sys
sys.stdin = open("노드의거리.txt", "r")

def bfs(matrix,S,G):
    global V
    visited = [0]*(V+1)
    q = []
    result = 0
    q.append(S)
    visited[S] = 1
    
    while q:
        sq = q[:]
        q = []
        print(sq)
        result += 1
        while sq:
            t = sq.pop(0)
            for i in range(len(matrix[t])):
                if matrix[t][i] == 1 and not visited[i]:
                    if i == G:
                        visited[i] = 1
                        return result
                    else:
                        q.append(i)
                        visited[i] = 1
    return 0


T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int,input().split())
    node = [list(map(int,input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    matrix = [[0]*(V+1) for _ in range(V+1)]

    for i in range(len(node)):
        matrix[node[i][0]][node[i][1]] = 1
        matrix[node[i][1]][node[i][0]] = 1
    
    print(f'#{test_case} {bfs(matrix,S,G)}')