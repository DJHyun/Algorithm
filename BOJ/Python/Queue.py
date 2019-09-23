def count_student(q):
    res = []
    for i in q:
        if i != 0:
            res.append(i)
    return print(f'학생 줄 : {res}')


my_chu = 20


stu = 0
count,c = [0] * 20,0
q = [0] * 23
f, r = -1, -1

while my_chu > 0:
    stu += 1

    if c != 0:
        print(f'{c}번 학생 : 다시 줄을 선다.')
        r += 1
        q[r] = c
        count_student(q)
    print(f'{stu} 번 학생 : 입장하여 줄을 선다.')
    r += 1
    q[r] = stu
    count_student(q)
    f += 1
    print(f'{q[f]}번 학생 : 줄에서 나와 ...')
    c = q[f]
    q[f] = 0
    count_student(q)
    count[c] += 1
    print(f'{c}번 학생 : 선생님한테 사탕 {count[c]}개를 받는다.')
    my_chu -= count[c]
    print(f'===== 남은 사탕의 개수는 {my_chu}개다.')
    print()

print(f'{c}번 학생')