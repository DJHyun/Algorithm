def back(a, k, check, sum):
    c = [0] * (check + 1)

    if sum == 10:
        for i in range(1, k + 1):
            print(number[a[i]], end=' ')
        print()
    elif sum >= 11:
        return
    else:
        k += 1
        ncandi = candi(a, k, check, c)
        for i in range(ncandi):
            a[k] = c[i]
            back(a, k, check, sum + number[a[k]])

def candi(a, k, check, c):
    in_perm = [0] * (check + 1)

    for i in range(1, k):
        for j in range(a[i], -1, -1):
            in_perm[j] = 1

    ncandi = 0
    for i in range(check):
        if not in_perm[i]:
            c[ncandi] = i
            ncandi += 1

    return ncandi

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [0] * (len(number) + 1)

back(a, 0, len(number), 0)
