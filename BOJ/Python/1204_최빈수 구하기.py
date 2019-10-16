# baekjoon source = "https://www.acmicpc.net/problem/1204"
T = int(input())

for i in range(1, T + 1):
    input()
    score = [0] * 101
    arr = list(map(int,input().strip().split(" ")))
    for j in range(1000):
        score[arr[j]] += 1

    max_ = 0;
    result = 0
    for k, v in enumerate(score):
        if max_ <= v:
            max_ = v
            result = k

    print("#{} {}".format(i,result))