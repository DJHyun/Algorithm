# source = www.programmers.co.kr

from collections import deque

def solution(priorities, location):
    answer = 1
    dq = deque()

    for i in range(len(priorities)):
        dq.append([i, priorities[i]])
    priorities.sort()
    priorities.reverse()
    max_ = priorities[answer - 1]
    while True:
        q = dq.popleft()
        if q[1] == max_:
            if q[0] == location:
                print(answer)
                return answer
            answer += 1
            max_ = priorities[answer - 1]
        else:
            dq.append(q)

solution([2, 1, 3, 2], 2)
solution([1, 1, 9, 1, 1, 1], 0)
