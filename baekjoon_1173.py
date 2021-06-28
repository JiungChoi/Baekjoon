import sys

N, m, M, T, R = map(int, sys.stdin.readline().split())
X = m
ex_cnt = 0
cnt = 0

if (m+T > M):
    print(-1)
    
while not (m+T > M):
    if X + T <= M:
        X += T
        ex_cnt +=1
    else:
        if X-R < m:
            X = m
        else:
            X -= R
    cnt +=1

    if N == ex_cnt:
        print(cnt)
        break