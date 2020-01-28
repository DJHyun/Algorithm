# source = www.programmers.co.kr

def solution(participant, completion):
    map = {}
    for i in range(len(participant)):
        if participant[i] not in map:
            map[participant[i]] = 1
        else:
            map[participant[i]] += 1

        if i < len(completion):
            if completion[i] not in map:
                map[completion[i]] = 1
            else:
                map[completion[i]] += 1

    for i in map.items():
        if i[1]%2 != 0:
            return i[0]

solution(['leo', 'kiki', 'eden'], ['eden', 'kiki'])
solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])
solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])
