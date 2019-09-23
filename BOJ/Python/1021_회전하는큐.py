# baekjoon source = "https://www.acmicpc.net/problem/1021"
import sys

N, M = map(int,sys.stdin.readline().split())
q = list(range(1,N+1))
pop_, result = list(map(int,sys.stdin.readline().split())), 0

for i in pop_:
    
    if i == q[0]:
        q = q[1:]
    else:
        if q.index(i) <= len(q)//2:
            while q[0] != i:        
                result += 1
                first = q[0]
                q = q[1:]
                q.append(first)
            q = q[1:]
        else:
            while q[0] != i:        
                result += 1
                last = q[len(q)-1]
                q = q[:len(q)-1]
                q.insert(0,last)
            q = q[1:]
print(result)