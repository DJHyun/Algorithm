# baekjoon source = "https://www.acmicpc.net/problem/4344"

T = int(input())

for t in range(T):
    numbers = input().split(' ')
    N = int(numbers[0])
    numbers.remove(str(N))
    sum_score = sum(map(int,numbers))
    avg = sum_score/N
    cnt = 0

    for i in numbers:
        if float(i) > avg:
            cnt +=1
    
    print('{:.3f}%'.format(cnt/N*100))
