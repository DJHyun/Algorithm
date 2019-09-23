import sys

sys.stdin = open("2056_연월일달력.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    nums = list(input())

    y = ''.join(nums[:4])
    m = ''.join(nums[4:6])
    d = ''.join(nums[6:8])

    if m <= '00' or m >= '13' or d <= '00' or d >= '32':
        print(f'#{test_case} {-1}')
    else:
        if m == '02':
            if d >= '01' and d <= '28':
                print(f'#{test_case} {y}/{m}/{d}')
            else:
                print(f'#{test_case} {-1}')
        elif m == '01' or m == '03' or m == '05' or m == '07' or m == '08' or m == '10' or m == '12':
            if d >= '01' and d <= '28':
                print(f'#{test_case} {y}/{m}/{d}')
            else:
                print(f'#{test_case} {-1}')
        else:
            if d >= '01' and d <= '28':
                print(f'#{test_case} {y}/{m}/{d}')
            else:
                print(f'#{test_case} {-1}')

