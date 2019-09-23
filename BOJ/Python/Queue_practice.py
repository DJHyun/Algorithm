def bfs(number):
    visited = [0] * (max(node)+1)
    que = []

    que.append(1)
    visited[1] = 1
    
    while que:
        t = que.pop(0)
        print(t)
        for i in range(len(number[t])):
            if not visited[i] and number[t][i] == 1:
                que.append(i)
                visited[i] = 1


node = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]
number = [[0]*(max(node)+1) for _ in range(max(node)+1)]
for i in range(0,(len(node)),2):
    number[node[i]][node[i+1]] = 1
bfs(number)


    