def stack_push(x):
    global top

    top += 1
    if top > len(stack):
        print("overflow")
    else:
        stack[top] = x

def stack_pop():
    global top

    if top == -1:
        return "underflow"
    else:
        top -= 1
        return stack[top+1]

stack = [0]*10
top = -1


stack_push(10)
stack_push(23)
stack_push('13')
stack_push([1,2,3])
print(stack)
print(stack_pop())
print(stack_pop())
print(stack_pop())
print(stack_pop())
print(stack_pop())
print(top)
print(stack)
