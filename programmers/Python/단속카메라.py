# source = www.programmers.co.kr

def solution(routes):
    answer = 1
    routes = sorted(routes, key=lambda x: (x[0], x[1]))
    standard = routes[0][1]

    for i in range(1, len(routes)):
        if standard >= routes[i][0]:
            standard = min(standard, routes[i][1])
        else:
            answer += 1
            standard = routes[i][1]
    return answer

solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]])
solution([[1, 2], [3, 4], [5, 6]])
