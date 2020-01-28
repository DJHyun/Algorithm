# source = www.programmers.co.kr

def solution(heights):
    len_ = len(heights)
    answer = [0]*len_

    for i in range(len_-1,-1,-1):
        for j in range(i,-1,-1):
            if heights[i] < heights[j]:
                answer[i] = (j+1)
                break

    return answer

solution([6, 9, 5, 7, 4])
solution([3, 9, 9, 3, 5, 7, 2])
solution([1, 5, 3, 6, 7, 6, 5])
