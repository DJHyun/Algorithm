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

def check(x, y):
    if x < 0 or x > n - 1: return False
    if y < 0 or y > n - 1: return False
    return True

t = int(input())
n = int(input())
arr = [input().strip().split() for _ in range(n)]

for tc in range(t):
    a, b, m = map(int, input().split())
    a -= 1
    b -= 1
    result = 0

    for i in range(m):
        index = arr[a][b]
        if index[0] == 'N':
            a -= int(index[1])
        elif index[0] == 'S':
            a += int(index[1])
        elif index[0] == 'E':
            b += int(index[1])
        else:
            b -= int(index[1])

        if check(a,b):
           continue
        else:
            result = 10000
            break
    else:
        result = (int(index[1])*1000)

    print('#{} {}'.format(tc+1,result))