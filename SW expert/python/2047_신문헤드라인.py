import sys
sys.stdin = open("2047_신문헤드라인.txt","r")

for i in list(input()):
    if i.islower():
        print(i.upper(),end='')
    else:
        print(i,end='')