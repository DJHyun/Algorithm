# source = www.programmers.co.kr

def solution(clothes):
    answer = 0
    c = {}

    for i in range(len(clothes)):
        if clothes[i][1] not in c:
            c[clothes[i][1]] = [clothes[i][0]]
        else:
            c[clothes[i][1]].append(clothes[i][0])

    s = 1
    for i in c.items():
        len_ = len(i[1])
        answer += len_
        s *= len_

    if len(c) > 1:
        answer += s
    return answer

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])