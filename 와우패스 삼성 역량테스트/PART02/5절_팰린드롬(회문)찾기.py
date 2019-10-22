'''
6
IAEFGSADAOFSOSPIPOKTOOTSCIVIC
SAQLANGUAGEOFCOMPUTER
SOFTWAREPROGRAMING
NETWORKSECURITY
DATAMININGSTUDY
ILOVECOMPUTER
'''

def solution(x, y):
    check = s[x:y]
    re = check[::-1]
    if check == re:
        result.append(''.join(check))
        return True
    return False

t = int(input())
for tc in range(t):
    s = list(input().strip())
    result = []
    count = 0

    for i in range(3, len(s) + 1):
        for j in range(0, len(s) - i + 1):
            if solution(j, j + i):
                count += 1

    if result:
        print(' '.join(result),',',count)
    else:
        print(0)