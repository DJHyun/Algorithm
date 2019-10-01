# source = www.programmers.co.kr

def solution(jobs):
    answer = 0
    jobs.sort()
    check = jobs[0][0]
    q = jobs
    while q:
        t = q.pop(0)
        answer += (check - t[0] + t[1])
        check += t[1]
        i = 0
        for a in range(len(q)):
            if q[a][0] > check:
                i -= 1
                break
            i += 1
        q = sorted(q[:i+1], key=lambda x: x[1]) + q[i + 1:]

        if q and check < q[0][0]:
            check += (q[0][0] - check)
    return answer // (len(jobs) + 1)

print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]]))
print(solution([[1, 9], [1, 4], [1, 5], [1, 7], [1, 3]]))
print(solution([[0, 5], [1, 2], [5, 5]]))
print(solution([[0, 3], [1, 9], [500, 6]]))
print(solution([[0, 6], [0, 8], [7, 1]] ))
