# source = www.programmers.co.kr

def solution(budgets, M):
    left = min(budgets)
    right = sum(budgets)
    mid = (left + right) // 2

    while True:
        print(left,mid,right)
        if left > right:
            break
        answer = 0
        for i in budgets:
            if mid < i:
                answer += mid
            else:
                answer += i
        if answer > M:
            right = mid-1
            mid = (left + right) // 2
        elif answer == M:
            break
        else:
            left = mid+1
            mid = (left + right) // 2

    print(mid)
    return mid

print(solution([5,5,5,15,25], 50))
print(solution([120, 110, 140, 150]	,485))
print(solution([5,5,5,5,15,30],62))
print(solution([1,2,3,4,5,6,7,8,9,10], 56))
print(solution([9, 8, 5, 6, 7] ,5))