def solution(tickets):
    global dic
    dic = {}
    answer = []

    for i in range(len(tickets)):
        if tickets[i][0] not in dic:
            dic[tickets[i][0]] = [tickets[i][1]]
        else:
            dic[tickets[i][0]].append(tickets[i][1])

    for i in tickets:
        print(i)
    print(dic)

    return answer

dic = {}
print(solution([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
