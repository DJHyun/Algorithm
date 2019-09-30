# source = www.programmers.co.kr

def solution(budgets, M):
    left = min(budgets)
    right = max(budgets)
    mid = (left + right) // 2
    while True:
        if left >= right:
            break
        answer = 0
        for i in budgets:
            if mid < i:
                answer += mid
            else:
                answer += i
            if answer > M:
                right = mid - 1
                mid = (left + right) // 2
                break
        left = mid + 1
        mid = (left + right) // 2

    return mid

print(solution([120, 110, 140, 150], 485))
