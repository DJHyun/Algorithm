# source = www.programmers.co.kr

def solution(genres, plays):
    answer = []
    len_ = len(genres)
    song = {}
    for i in range(len_):
        if genres[i] not in song:
            song[genres[i]] = [plays[i], [plays[i], i]]
        else:
            song[genres[i]][0] += plays[i]
            song[genres[i]].append([plays[i], i])

    song = sorted(song.values(), key=lambda x: -x[0])

    for i in range(len(song)):
        if len(song[i]) == 2:
            answer.append(song[i][1][1])
            continue
        ne = sorted(song[i][1:], key=lambda x: (-x[0], x[1]))

        for j in range(2):
            answer.append(ne[j][1])

    return answer

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])
