check = '0000000111100000011000000111100110000110000111100111100111111001100111'

i = 0
while True:
    if i + 7 == len(check) + 7:
        break
    else:
        num = check[i:i + 7]

        i += 7

        print(num)

        result = 0
        for a in range(len(num) - 1, -1, -1):
            result += int(num[a]) * 2 ** (len(num)-a-1)

        print(result)
