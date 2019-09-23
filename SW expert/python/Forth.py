import sys
sys.stdin = open("Forth.txt", "r")

def my_isdigit(s):
    try:
        int(s)
        return True
    except:
        return False

T = int(input())
for test_case in range(1, T + 1):
    str_ = input().split()
    stack, top = [0]*len(str_), -1

    for s in str_:
        if my_isdigit(s):
            top += 1
            stack[top] = int(s)
        else:
            if s == '.':
                if top == 0:
                    print(f'#{test_case} {stack[0]}')
                    break
                else:
                    print(f'#{test_case} error')
                    break
            else:
                if top < 1:
                    print(f'#{test_case} error')
                    break
                else:
                    if s == '*':
                        stack[top-1] = stack[top-1] * stack[top]
                        stack[top] = 0
                        top -= 1
                    elif s == '/':
                        stack[top-1] = stack[top-1] // stack[top]
                        stack[top] = 0
                        top -= 1
                    elif s == '+':
                        stack[top-1] = stack[top-1] + stack[top]
                        stack[top] = 0
                        top -= 1
                    else:
                        stack[top-1] = stack[top-1] - stack[top]
                        stack[top] = 0
                        top -= 1       