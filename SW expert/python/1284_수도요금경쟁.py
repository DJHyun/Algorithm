# SW Expert Academy
import sys
sys.stdin = open('input (3).txt','r')

T = int(input())
for test_case in range(1, T + 1):
    p,q,r,s,w = map(int,input().split())
    one = p * w
    two = 0

    if r >= w:
        two = q
    else:
        two = q + (w-r)*s
    
    print(f'#{test_case} {min(one,two)}')

