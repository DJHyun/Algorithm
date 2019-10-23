'''
6
RRGGBB
RG
RGBRGB
RGGGBB
BBBRRRRRGGGGGG
GGGGRRRBBBBBBBB
'''

t = int(input())
for tc in range(1, t+1):
    s = input().strip()

    start = s[0]
    score = 1
    result = 0
    for i in range(1,len(s)):
        if s[i] == start:
            score += 1
        else:
            result = max(score,result)
            score = 1
            start = s[i]
    result = max(score,result)

    print(len(s)-result)