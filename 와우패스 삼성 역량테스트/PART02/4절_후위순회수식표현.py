'''
6
21+(3-4)*(8-3)*(3+1)/2
(3+4)*8-(3+7)/2
(11-8)/3+7*2
11+(14-3+2)*2-3+(1+6-5)
(1+2+3+4+5+6)/3+4+5
1*2+3/2+4-4+5+6+6+5-(5*7-5)
'''

t = int(input())
method = ['+', '-', '*', '/']
for tc in range(t):
    arr = list(input().strip())

    num = ''
    new_arr = []
    for i in arr:
        if i not in method and i != '(' and i != ')':
            num += i
        else:
            if num:
                new_arr.append(num)
                num = ''
                new_arr.append(i)
            else:
                new_arr.append(i)
    if num:
        new_arr.append(num)

    numbers = []
    mt = []
    top = -1

    for i in new_arr:
        if i in method:
            if not mt:
                mt.append(i)
            elif i == '+' or i == '-':
                if '(' not in mt:
                    numbers += mt
                    mt.clear()
                    mt.append(i)
                else:
                    mt.append(i)
            elif i == '*' or i == '/':
                if '(' not in mt:
                    for go in range(len(mt) - 1, -1, -1):
                        if mt[go] == '*' or mt[go] == '/':
                            numbers += mt.pop()
                        else:
                            break
                    mt.append(i)
                else:
                    mt.append(i)
        elif i == '(':
            mt.append(i)
        elif i == ')':
            for go in range(len(mt) - 1, -1, -1):
                if mt[go] != '(':
                    numbers += mt.pop()
                else:
                    mt.pop()
                    break
        else:
            numbers.append(i)
        # print(numbers)
        # print(mt)
    while mt:
        numbers += mt.pop()

    print(' '.join(numbers))
