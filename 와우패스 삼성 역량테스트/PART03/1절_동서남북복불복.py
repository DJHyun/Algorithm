'''
3
7
E3 S2 S4 S5 E2 S1 S5
N2 S3 S2 E1 N3 W4 N1
W1 N1 E3 W3 S3 W1 S3
E3 S2 N2 S2 E1 N2 W3
N3 E3 S1 N1 W3 E1 W1
E1 N2 W1 N3 S2 N3 W5
N5 E1 N4 W3 N5 W1 S1
3 4 3
2 3 4
4 6 5
'''

t = int(input())
n = int(input())
arr = [list(input().split()) for _ in range(n)]
for tc in range(t):
    x,y,z = map(int,input().split())
    x -= 1
    y -= 1
    for i in range(z):
        go = arr[x][y]
        go = list(go)
        go[1] = int(go[1])
        if go[0] == 'N':
            x -= go[1]
        elif go[0] == 'S':
            x += go[1]
        elif go[0] == 'E':
            y += go[1]
        else:
            y -= go[1]

        if x < 0 or x > n -1:
            print(10000)
            break
        if y < 0 or y > n -1:
            print(10000)
            break
    else:
        print(int(arr[x][y][1])*1000)