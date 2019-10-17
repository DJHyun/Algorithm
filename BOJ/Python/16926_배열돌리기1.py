# baekjoon source = "https://www.acmicpc.net/problem/16926"
'''
4 4 2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
'''
import sys

n, m, r = map(int, sys.stdin.readline().split())
arr = [sys.stdin.readline().strip().split() for _ in range(n)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

for count in range(min(n,m) // 2):
    x = len(arr[count]) - (count * 2)
    y = len(arr) - (count * 2)
    result_r = r % (2 * x + (y - 2) * 2)

    for go in range(result_r):
        index = 0
        i, j = count,count
        c = 0
        while c <= 3:
            i += dx[index]
            j += dy[index]
            arr[count][count], arr[i][j] = arr[i][j], arr[count][count]
            if (i == count and j == count) or (i == (n-count)-1 and j == count) or (i == (n-count)-1 and j == (m-count)-1) or (i == count and j == (m-count)-1):
                index += 1
                c += 1

for aa in arr:
    print(' '.join(aa))
