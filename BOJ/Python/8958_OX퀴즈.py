# baekjoon source = "https://www.acmicpc.net/problem/8958"

T = int(input())

for t in range(T):
    ox = list(input())
    result = 0
    cnt = 0

    for i,s in enumerate(ox):
        if i == 0:
            if s == 'O':
                result += 1
                cnt += 1
        else:
            if s == 'O':
                if ox[i-1] == 'O':
                    cnt += 1
                    result += cnt
                else:
                    cnt += 1
                    result += 1
            else:
                cnt = 0 
    print(result)