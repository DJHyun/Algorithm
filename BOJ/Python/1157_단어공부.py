# baekjoon source = "https://www.acmicpc.net/problem/1157"

s = list(input().lower())
list_ = []
result = []
cnt = 0

for i in s:
    if i not in list_:
        list_.append(i)
        result.append(1)
    else:
        result[list_.index(i)] += 1

for i in result:
    if max(result) == i:
        cnt += 1
if cnt > 1:
    print('?')
else:
    print(list_[result.index(max(result))].upper())