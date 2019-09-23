import sys

'''
3
6
8
15

4 6
5 2
8 14
'''
# sys.stdin = open("input.txt", "r")

def inorder(T):
    global idx
    if T <= len(number):
        inorder(T*2)
        idx += 1
        result[T] = number[idx]
        inorder(T*2+1)

T = int(input())
for test_case in range(1, T + 1):
    number = [x for x in range(1, int(input()) + 1)]
    result = [0]* (len(number)+1)
    n = len(number) // 2
    mid = len(number) // 2 + 1
    idx = -1

    inorder(1)
    print('#{} {} {}'.format(test_case, result[1], result[n]))