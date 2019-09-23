# baekjoon source = "https://www.acmicpc.net/problem/2108"
import sys

T = int(sys.stdin.readline())
mlist, mdict = [], {}
msum, mmin, mmax = 0,4001,-4001

for test_case in range(T):
    mlist.append(int(sys.stdin.readline()))

mlist.sort()
for i in range(len(mlist)):
    msum += mlist[i]

    if mmin > mlist[i]:
        mmin = mlist[i]
    
    if mmax < mlist[i]:
        mmax = mlist[i]

    if mlist[i] not in mdict:
        mdict[mlist[i]]= 1
    else:
        mdict[mlist[i]] += 1

print(round(msum/len(mlist) + 0.1 if str(msum/len(mlist))[2]=='5' else msum/len(mlist)))
print(mlist[int(len(mlist)/2)])

max_mdict = max(mdict.values())

for v in list(mdict):
    if mdict[v] != max_mdict:
        mdict.pop(v)

if len(mdict) == 1:
    print(list(mdict)[0])
else:
    for i,v in enumerate(mdict.keys()):
        if i == 1:
            print(v)
            break

print(mmax - mmin)
# print(mlist, msum, mavg, mmin, mmax, mcnt)