# baekjoon source = "https://www.acmicpc.net/problem/2909"

price, count = map(int,input().split())
money = 10**count

price = list(str(price))

if price[len(price)-1-(count-1)] == '5':
    price[len(price)-1-(count-1)] = '6'

price = int(''.join(price))
price = round(price,-count)
print(price)