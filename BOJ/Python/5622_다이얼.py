# baekjoon source = "https://www.acmicpc.net/problem/5622"

import sys

A = list(sys.stdin.readline().strip().lower())
number = ''
for i in A:
    if i in("a", "b", "c"):
        number += "2"
    elif i in ("d", "e", "f"):
        number += "3"
    elif i in ("g", "h", "i"):
        number += "4"
    elif i in ("j", "k", "l"):
        number += "5"
    elif i in ("m", "n", "o"):
        number += "6"
    elif i in ("p", "q", "r", "s"):
        number += "7"
    elif i in ("t", "u", "v"):
        number += "8"
    elif i in ("w", "x", "y", "z"):
        number += "9"
    else:
        number += "0"
result = 0
for i in number:
    result += int(i)+1

print(result)