# baekjoon source = "https://www.acmicpc.net/problem/2675"

for t in range(int(input())):
    list_ = input().split()
    r,s = int(list_[0]),list_[1]
    result = ''

    for i in s:
        result += i*r

    print(result)
