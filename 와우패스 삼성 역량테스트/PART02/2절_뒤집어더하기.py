'''
8
121
120
46
12345
45678
111
9
3
'''

import sys

t = int(sys.stdin.readline())
for tc in range(t):
    n = sys.stdin.readline().strip()
    revers_ = n[::-1]
    result = int(n) + int(revers_)
    check = int(str(result)[::-1])
    print('yes' if result == check else 'no')
