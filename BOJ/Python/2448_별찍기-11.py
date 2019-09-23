# baekjoon source = "https://www.acmicpc.net/problem/2448"

import math

T = int(input())
k = int(math.log(T/3,2))
print(k)
star = ['  *   ',' * *  ','***** ']

for k in range(k):
    for i in range(len(star)):
        star.append(star[i] + star[i])
        star[i] = " "*(2**k*3) +star[i]+" "*(2**k*3)

for i in star:
    print(i)   

    
print(len(star))
 