'''
3
13 4 1 8 1 6 2 10 2 5 3 9 3 1 4 7 4 8 4 6 5 3 6 7 6 10 6
15 1 1 6 1 9 1 3 2 5 2 8 2 4 3 7 3 10 3 2 4 6 4 8 4 3 5 5 5 7 5
6 1 1 5 1 2 2 4 2 3 3 5 3
'''

def solution(x, y):
    q = [[x, y]]
    while q:
        t = q.pop(0)
        tx = t[0] + 1
        ty = t[1]
        if tx == input_[0] + 1:
            return ty
        if arr[tx][ty] == 1:
            q.append([tx, ty])
        elif arr[tx][ty] == 2:
            if ty % 2:
                if arr[tx][ty + 1] == 2:
                    q.append([tx, ty + 1])
                elif arr[tx][ty - 1] == 2:
                    q.append([tx, ty - 1])
            else:
                if arr[tx][ty - 1] == 2:
                    q.append([tx, ty - 1])
                elif arr[tx][ty + 1] == 2:
                    q.append([tx, ty + 1])
t = int(input())
for tc in range(1, t + 1):
    input_ = list(map(int, input().split()))
    print(input_)
    arr = [[1] * input_[0] for _ in range(input_[0] + 1)]
    number = 0
    for i in range(1, len(input_) - 1, 2):
        print(i, i + 1, input_[i], input_[i + 1])
        arr[input_[i]][input_[i + 1]] = 2
        arr[input_[i]][input_[i + 1] + 1] = 2
        number = max(number, input_[i + 1] + 1)

    for i in arr:
        print(i)

    result = [0] * (number + 1)

    for i in range(1, number + 1):
        print(i)
        result[i] = solution(0, i)
    print(result)
