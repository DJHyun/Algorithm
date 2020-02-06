# baekjoon source = "https://www.acmicpc.net/problem/15650"

import sys
from itertools import combinations

n,m = map(int,sys.stdin.readline().split())

[print(*it) for it in combinations(range(1,n+1),m)]