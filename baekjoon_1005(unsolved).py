import sys

T = int(sys.stdin.readline())
for _ in range(T):
    cnt = 0
    N, K = map(int, sys.stdin.readline().split())
    D = list(map(int, sys.stdin.readline().split()))

    stair = [[] for _ in range(N)]
    
    print(f'{stair}')

    for _ in range(K):
        I, You = map(int, sys.stdin.readline().split())
        stair[I].append(You)
    #print(f'{stair}')
    #print(f'{stair[1][0]}')
    #print(f'{stair[1][1]}')
    #print(f'{stair[1]}')
    W = int(sys.stdin.readline())
    


        