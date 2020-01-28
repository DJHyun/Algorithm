# source = www.programmers.co.kr

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = []
    len_ = len(truck_weights)
    index = 0
    size = 0

    while index <= len_:
        if not bridge:
            if index >= len_:
                break
            bridge.append([1, truck_weights[index]])
            size += truck_weights[index]
            index += 1
        else:
            id = 0
            while id < len(bridge):
                if bridge[id][0] + 1 > bridge_length:
                    size -= bridge[id][1]
                    bridge.pop(id)
                else:
                    bridge[id][0] += 1
                    id += 1

            if index < len_:
                if size + truck_weights[index] <= weight:
                    bridge.append([1, truck_weights[index]])
                    size += truck_weights[index]
                    index += 1

        answer += 1

    return answer

solution(2, 10, [7, 4, 5, 6])
solution(100, 100, [10])
solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
