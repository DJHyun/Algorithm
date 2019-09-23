import sys

sys.stdin = open("2050_알파벳을숫자로변환.txt", "r")

[print(ord(i) - 64, end=' ') for i in list(input())]
