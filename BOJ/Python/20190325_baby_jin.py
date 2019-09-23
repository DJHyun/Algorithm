one = [1,0,1,1,2,3]
'''
1,2,4,7,8,3
6,6,7,7,6,7
0,5,4,0,6,0
1,0,1,1,2,3
'''

check = {}

for i in one:
    if i not in check:
        check[i] = 1
    else:
        check[i] += 1

check = sorted(check.items())
print(check)

result = []
for i in range(len(check)):
    if check[i][1] >= 3:
        result.append('triplet')
        check[i] = (check[i][0],check[i][1]-3)

    if len(result) == 2:
        print('baby_jin!!')
        break


else:
    i = 0
    while i < len(check)-2:
        if check[i][0] + 1 == check[i+1][0]:
            if check[i+1][0] + 1 == check[i+2][0]:
                result.append('run')
                i += 2
            else:
                i += 1
        else:
            i += 1

        if len(result) == 2:
            print('baby_jin!')
            break

if len(result) == 1:
    print(''.join(result))





