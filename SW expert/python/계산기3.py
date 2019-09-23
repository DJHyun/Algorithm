import sys
sys.stdin = open("계산기3.txt", "r")

for test_case in range(1, 11):
    le = int(input())
    st = input()
    stack = [0] * le; top = -1
    result = [0] * (le-st.count(')')-st.count('(')); rtop = -1

    for i in st:
        if i == '(':
            top += 1
            stack[top] = i
        elif i == ')':
            while stack[top] != '(':
                rtop += 1
                result[rtop] = stack[top]
                top -= 1
            else:
                stack[top] = 0
                top -= 1
        elif i == '*':
            if stack[top] == '*':
                rtop += 1
                result[rtop] = '*'
            else:
                top += 1
                stack[top] = i
        elif i == '+':
            if stack[top] == '*':
                rtop += 1
                result[rtop] = '*'
                stack[top] = 0
                top -= 1
            if stack[top] == '+':
                rtop += 1
                result[rtop] = '+'
            else:
                top += 1
                stack[top] = i
        else:
            rtop += 1
            result[rtop] = i
    while top != -1:
        rtop += 1
        result[rtop] = stack[top]
        top -= 1
    
    stack = [0] * len(result); top = -1
    
    for s in result:
        if s.isdigit():
            top += 1
            stack[top] = int(s)
        else:
            if s == '*':
                stack[top-1] = stack[top-1] * stack[top]
                stack[top] = 0
                top -= 1
            elif s == '+':
                stack[top-1] = stack[top-1] + stack[top]
                stack[top] = 0
                top -= 1
    print(f'#{test_case} {stack[0]}')