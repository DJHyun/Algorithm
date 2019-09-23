# baekjoon source = "https://www.acmicpc.net/problem/5373"
import datetime

a = list(map(int, input().split()))

time_one = datetime.datetime(2019, 1, 1, a[0], a[1], a[2])
time_two = datetime.datetime(2019, 1, 1, a[3], a[4], a[5])
result = list(map(int,str(time_two - time_one).split(':')))
print(result[0],result[1],result[2])

b = list(map(int, input().split()))

time_one = datetime.datetime(2019, 1, 1, b[0], b[1], b[2])
time_two = datetime.datetime(2019, 1, 1, b[3], b[4], b[5])
result = list(map(int,str(time_two - time_one).split(':')))
print(result[0],result[1],result[2])

c = list(map(int, input().split()))

time_one = datetime.datetime(2019, 1, 1, c[0], c[1], c[2])
time_two = datetime.datetime(2019, 1, 1, c[3], c[4], c[5])
result = list(map(int,str(time_two - time_one).split(':')))
print(result[0],result[1],result[2])