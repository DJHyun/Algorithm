# source = www.programmers.co.kr


def find(x):
    if mst[x] == x:
        return x
    return find(mst[x])

def solution(n, costs):
    global mst

    answer = 0
    mst = [i for i in range(n)]
    costs = sorted(costs, key=lambda x: x[2])
    for i in costs:
        a = find(i[0])
        b = find(i[1])
        if a != b:
            answer += i[2]
        mst[b] = a

    return answer

mst = []
print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
