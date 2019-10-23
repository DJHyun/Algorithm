'''
5
SAQLANGUAGEOFCOMPUTER
SOFTWAREPROGRAMING
ILOVECOMPUTER
SAQTEST
NETWORKSECURITY
DATAMININGSTUDY
'''

t = int(input())
s = input().strip()
print(s)
len_s = len(s)
for tc in range(1, t + 1):
    compare = input().strip()
    check = [[] for _ in range(len(compare) - 1)]
    check[0].append(compare)
    result = []
    if check[0][0] not in s:
        for i in range(len(check) - 1):
            for j in range(len(check[i])):
                a = check[i][j][0:len(check[i][j]) - 1]
                if a not in check[i + 1]:
                    check[i + 1].append(a)
                    if a in s:
                        result.append(a)
                b = check[i][j][1:]
                if b not in check[i + 1]:
                    check[i + 1].append(b)
                    if b in s:
                        result.append(b)
    else:
        print('#', tc, compare, len(compare))

    print(result)

