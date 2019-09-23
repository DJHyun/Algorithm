def select_sort(idx, a):
    if idx > len(arr) - 2:
        return

    arr[idx], arr[a] = arr[a], arr[idx]

    se_min = arr.index(min(arr[idx + 1:]))
    select_sort(idx + 1, se_min)

arr = [2, 1, 5, 4, 3, 20, 6, 7, 8, 18]
min_ = arr.index(min(arr))

print(f'변경전 : {arr}')
select_sort(0, min_)

print(f'변경후 : {arr}')