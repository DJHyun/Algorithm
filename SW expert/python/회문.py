import sys
sys.stdin = open("회문.txt", "r")

def my_palindrome(a):
    for i in range(len(a)//2):
        if a[i] != a[len(a)-1-i]:
            return False
    return True

T = int(input())
for test_case in range(1, T + 1):
    li = list(map(int,input().split()))
    N = li[0]
    M = li[1]
    st = []
    result = ''
    sv = []
    for i in range(N):
        st.append(list(input()))
    
    for i in range(len(st)):
        sv.append([])
        for j in range(len(st)):
            sv[i].append(st[j][i])
            
    for i in st:
        if len(i) == M:
            if my_palindrome(i):
                st = i
                break
        elif len(i) > M:
            for j in range(len(i) - M+1):
                if my_palindrome(i[j:M+j]):
                    st = i[j:M+j]
                    break
    else:
        for i in sv:
            if len(i) == M:
                if my_palindrome(i):
                    st = i
                    break
            elif len(i) > M:
                for j in range(len(i) - M+1):
                    if my_palindrome(i[j:M+j]):
                        st = i[j:M+j]
                        break
    
    for re in st:
        result += re
    print(f'#{test_case} {result}')