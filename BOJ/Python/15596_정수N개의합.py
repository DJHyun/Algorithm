# baekjoon source = "https://www.acmicpc.net/problem/15596"

def solve(a):
    ans = 0
    for i in range(len(a)):
        ans += a[i]
    return ans

print(solve([1,2,3,4]))