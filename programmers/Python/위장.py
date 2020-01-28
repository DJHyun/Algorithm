# source = www.programmers.co.kr

def solution(clothes):
    answer = 1
    c = {}

    for i in range(len(clothes)):
        if clothes[i][1] not in c:
            c[clothes[i][1]] = [clothes[i][0]]
        else:
            c[clothes[i][1]].append(clothes[i][0])

    for i in c:
        answer *= (len(c[i])+1)


    answer -= 1
    return answer

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])
solution([["crow_mask", "face"], ["blue_sunglasses", "face1"], ["smoky_makeup", "face2"]])
solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"],
          ["crow_mask", "face1"], ["blue_sunglasses", "face1"], ["smoky_makeup", "face1"],
          ["crow_mask", "face2"], ["blue_sunglasses", "face2"], ["smoky_makeup", "face2"],
          ["crow_mask", "face3"], ["blue_sunglasses", "face3"], ["smoky_makeup", "face3"],
          ["crow_mask", "face4"], ["blue_sunglasses", "face4"], ["smoky_makeup", "face4"],
          ["crow_mask", "face5"], ["blue_sunglasses", "face5"], ["smoky_makeup", "face5"],
          ["crow_mask", "face6"], ["blue_sunglasses", "face6"], ["smoky_makeup", "face6"],
          ["crow_mask", "face7"], ["blue_sunglasses", "face7"], ["smoky_makeup", "face7"],
          ["crow_mask", "face8"], ["blue_sunglasses", "face8"], ["smoky_makeup", "face8"],
          ["crow_mask", "face9"], ["blue_sunglasses", "face9"], ["smoky_makeup", "face9"]]
         )
