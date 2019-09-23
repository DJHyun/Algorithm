# baekjoon source = "https://www.acmicpc.net/problem/2941"

import sys

s = sys.stdin.readline().strip()
cnt = 0

if "c=" in s:
    s = s.replace("c=", "1")
if "c-" in s:
    s = s.replace("c-", "1")
if "dz=" in s:
    s = s.replace("dz=", "1")
if "d-" in s:
    s = s.replace("d-", "1")
if "lj" in s:
    s = s.replace("lj", "1")
if "nj" in s:
    s = s.replace("nj", "1")
if "s=" in s:
    s = s.replace("s=", "1")
if "z=" in s:
    s = s.replace("z=", "1")

print(len(s))
