# baekjoon source = "https://www.acmicpc.net/problem/4673"

result = list(range(1,10001))

for i in range(1,10001):
    if(len(str(i)) >=2 ):
        str_num = list(str(i))
    else:
        str_num = list(str(i))
    str_num = map(int,str_num)
    num = i + sum(str_num)
    if num in result:
        result.remove(num)

for i in result:
    print(i)


