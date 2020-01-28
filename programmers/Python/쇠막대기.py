# source = www.programmers.co.kr

from collections import deque

def solution(arrangement):
    answer = 0
    stack = deque()
    score = deque()
    for i in arrangement:
        if i == '(':
            stack.append(i)
            score.append(0)
        else:
            stack.pop()
            s = score.pop()
            if s != 0:
                answer += s+1
            else:
                for j in range(len(score)):
                    score[j] += 1

    print(answer)
    return answer

solution("()(((()())(())()))(())")
