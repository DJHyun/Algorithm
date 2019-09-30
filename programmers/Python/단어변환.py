# source = www.programmers.co.kr

def solution(begin, target, words):
    answer = 0

    if target in words:
        len_ = len(words)
        visited = [0] * len_
        while True:
            flag = True
            for i in range(len(begin)):
                if begin[i] != target[i]:
                    if flag:
                        flag = False
                    else:
                        break
            else:
                answer += 1
                break

            for i in range(len_):
                if not visited[i]:
                    flag = True
                    for j in range(len(begin)):

                        if begin[j] != words[i][j]:
                            if flag:
                                flag = False
                            else:
                                break
                    else:
                        begin = words[i]
                        visited[i] = 1
                        answer += 1
                        break

    return answer

print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
