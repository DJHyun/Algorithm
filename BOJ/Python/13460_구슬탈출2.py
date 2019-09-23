# baekjoon source = "https://www.acmicpc.net/problem/13460"

def check(x, y, a, b):
    global n,m
    if x < 0 or x > m - 1: return False
    if y < 0 or y > n - 1: return False
    if x == a and y == b: return 2
    if arr[x][y] == '.' or arr[x][y] == 'O': return 1
    return False

def bfs(a, b, c, d):
    tq = []
    tq.append([a, b, c, d])
    result = 0
    while tq:
        if result > 10:
            result = -1
            return result
        result += 1
        q = tq[:]
        tq.clear()
        while q:
            t = q.pop(0)
            for i in range(4):
                flag = False
                r_flag = False
                b_flag = False
                ta, tb, tc, td = -1, -1, -1, -1

                if check(t[0] + dx[i], t[1] + dy[i], t[2], t[3]) == 1:
                    ta = t[0] + dx[i]
                    tb = t[1] + dy[i]
                    while check(ta, tb, t[2], t[3]) == 1:
                        if arr[ta][tb] == 'O':
                            r_flag = True
                            ta = 20
                            tb = 20
                            break
                        ta += dx[i]
                        tb += dy[i]
                    if check(ta,tb,t[2],t[3]) == 2:
                        flag = True
                    ta -= dx[i]
                    tb -= dy[i]
                else:
                    flag = True

                if ta != -1 and tb != -1:
                    if check(t[2] + dx[i], t[3] + dy[i], ta, tb) == 1:
                        tc = t[2] + dx[i]
                        td = t[3] + dy[i]
                        while check(tc, td, ta, tb) == 1:
                            if arr[tc][td] == 'O':
                                b_flag = True
                                break
                            tc += dx[i]
                            td += dy[i]
                        tc -= dx[i]
                        td -= dy[i]
                else:
                    if check(t[2] + dx[i], t[3] + dy[i], t[0], t[1]) == 1:
                        tc = t[2] + dx[i]
                        td = t[3] + dy[i]
                        while check(tc, td, t[0], t[1]) == 1:
                            if arr[tc][td] == 'O':
                                b_flag = True
                                break
                            tc += dx[i]
                            td += dy[i]
                        tc -= dx[i]
                        td -= dy[i]

                if flag:
                    if tc != -1 and td != -1:
                        if check(t[0] + dx[i], t[1] + dy[i], tc, td) == 1:
                            ta = t[0] + dx[i]
                            tb = t[1] + dy[i]
                            while check(ta, tb, tc, td) == 1:
                                if arr[ta][tb] == 'O':
                                    r_flag = True
                                    break
                                ta += dx[i]
                                tb += dy[i]
                            ta -= dx[i]
                            tb -= dy[i]
                    else:
                        if check(t[0] + dx[i], t[1] + dy[i], t[2], t[3]) == 1:
                            ta = t[0] + dx[i]
                            tb = t[1] + dy[i]
                            while check(ta, tb, t[2], t[3]) == 1:
                                if arr[ta][tb] == 'O':
                                    r_flag = True
                                    break
                                ta += dx[i]
                                tb += dy[i]
                            ta -= dx[i]
                            tb -= dy[i]

                if r_flag and not b_flag:
                    if result > 10:
                        result = -1
                    return result
                elif not r_flag and not b_flag:
                    if ta == -1 or tb == -1:
                        new = [t[0], t[1]]
                    else:
                        new = [ta, tb]
                    if tc == -1 or td == -1:
                        new += [t[2], t[3]]
                    else:
                        new += [tc, td]
                    if new not in tq:
                        tq.append(new)

m, n = map(int, input().split())
arr = [list(input()) for _ in range(m)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

for i in range(m):
    for j in range(n):
        if arr[i][j] == 'R':
            arr[i][j] = '.'
            a, b = i, j
        if arr[i][j] == 'B':
            arr[i][j] = '.'
            c, d = i, j
print(bfs(a, b, c, d))
