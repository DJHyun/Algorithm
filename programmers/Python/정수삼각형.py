# source = www.programmers.co.kr

def solution(triangle):
    answer = 0
    memo = [[0] * (i + 1) for i in range(len(triangle))]

    memo[0][0] = triangle[0][0]
    len_ = len(triangle)
    for i in range(1,len_):
        for j in range(len(triangle[i-1])):
            for z in range(2):
                if z == 0:
                    if memo[i][j+z] < memo[i-1][j+z]+triangle[i][j+z]:
                        memo[i][j+z] = memo[i-1][j+z]+triangle[i][j+z]
                else:
                    if memo[i][j+z] < memo[i-1][j+z-1]+triangle[i][j+z]:
                        memo[i][j+z] = memo[i-1][j+z-1]+triangle[i][j+z]

    answer = max(memo[len_-1])

    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
