import sys

N, M = map(int, sys.stdin.readline().split())

arry = [[] for _ in range(N)]
for i in range(N):
    arry[i] +=  input()

ans = []
for i in range(N):
    for j in  range(M):
        for k in range(j+1,M):
            if arry[i][j] == arry[i][k]:
                if i + (k-j) < N:
                    if arry[i][j] == arry[i + (k-j)][j] and arry[i + (k-j)][j] == arry[i + (k-j)][k]:
                        ans.append((k-j+1)**2)
                    else:
                        pass
                else:
                    pass
            else:
                pass
            
if not ans:
    print('1')
else:
    print(max(ans))
