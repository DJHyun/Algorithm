import sys

sys.stdin = open('input (15).txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    check = []
    st = list(input())

    for s in range(len(st)):
        if st[s] not in check:
            check.append(st[s])
        else:
            if ''.join(check) == ''.join(st[s:s + len(check)]):
                break
            else:
                check.append(st[s])

    print(f'#{test_case} {len(check)}')
