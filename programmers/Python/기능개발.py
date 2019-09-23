"""
93 30 55
1 30 5
"""

def solution(progresses, speeds):
    na = [0] * len(progresses)
    top = -1
    len_ = len(progresses)
    for i in range(len_):
        if (100 - progresses[i]) % speeds[i] != 0:
            value = (100 - progresses[i]) // speeds[i] + 1
        else:
            value = (100 - progresses[i]) // speeds[i]
        top += 1
        na[top] = value
    answer = []

    for i in range(len_):
        if na[i] == -1:
            continue
        cnt = 1
        for j in range(i + 1, len_):
            if na[i] >= na[j]:
                cnt += 1
                na[j] = -1
            else:
                break
        answer.append(cnt)
    return answer

a = list(map(int, input().split()))
b = list(map(int, input().split()))
solution(a, b)
