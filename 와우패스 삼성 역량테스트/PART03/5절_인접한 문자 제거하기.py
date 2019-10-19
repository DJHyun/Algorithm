'''
5
SIEEILL
SH
AKHHKEA
HELLO
SCANNER
'''

t = int(input())
for tc in range(1, t + 1):
    s = input().strip()

    while True:
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                s = s[0:i]+s[i+2:]
                break
        else:
            break

    print(s)