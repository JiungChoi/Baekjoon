 sys
T import= int(input())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    arry = [[[] for _ in range(M)]for _ in range(N)]
    for _ in range(K):
        arry_x, arry_y = map(int, sys.stdin.readline().split())
        arry[arry_y][arry_x] = 1
    print(arry)
