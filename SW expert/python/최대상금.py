import sys

sys.stdin = open("최대상금.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    score, count = map(int, input().split())
    score = list(str(score))
    cnt = 0
    ct = 0
    cr = 0

    while cnt < count:
        if count < len(score):
            if ct < len(score):
                if count == 1:
                    max_ = max(score[ct:])
                    for i in range(len(score) - 1, ct - 1, -1):
                        if score[i] == max_:
                            idx = i
                            break
                    if score[idx] != score[ct]:
                        score[ct], score[idx] = score[idx], score[ct]
                    else:
                        cnt -= 1
                else:
                    max_ = max(score[ct:])
                    if score.count(max_) == 1:
                        for i in range(len(score) - 1, ct - 1, -1):
                            if score[i] == max_:
                                idx = i
                        if score[idx] != score[ct]:
                            score[ct], score[idx] = score[idx], score[ct]
                        else:
                            cnt -= 1
                    else:
                        min_ = min(score[:len(score) - cr])
                        if score.index(min_) != len(score)-1:

                            for i in range(len(score) - 1, ct - 1, -1):
                                if score[i] == max_:
                                    idx = i
                                    break
                            score[score.index(min_)], score[idx] = score[idx], score[score.index(min_)]
                            cr += 1
            ct += 1
        else:
            if ct < 4:
                max_ = max(score[ct:])
                for i in range(len(score) - 1, ct - 1, -1):
                    if score[i] == max_:
                        idx = i
                        break
                if score[idx] != score[ct]:
                    score[ct], score[idx] = score[idx], score[ct]
                else:
                    cnt -= 1
                ct += 1
            else:
                score[len(score) - 2], score[len(score) - 1] = score[len(score) - 1], score[len(score) - 2]

        cnt += 1

    print(f'#{test_case} {"".join(score)}')
