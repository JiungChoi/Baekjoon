import sys
INF = 11

V, E = map(int,sys.stdin.readline().split())
K = int(input())

#채워나갈 비교 배열
dist =[INF for _ in range(V)]
dist[K-1] = 0

#피비교배열
adj = [[INF for _ in range(V)] for _ in range(V)]

# E개의 경로와 가중치
for i in range(E):
    u, v, w = map(int,sys.stdin.readline().split())
    adj[u-1][v-1] = w

cmp_dist = dist[:]
for k in range(V):
    for i in range(V):
            dist[i] = min(dist[i],dist[cmp_dist.index(min(cmp_dist))] + adj[cmp_dist.index(min(cmp_dist))][i])
    cmp_dist = dist[:]
    
    for _ in range(k+1):
        cmp_dist[cmp_dist.index(min(cmp_dist))] = 10
for i in range(V):
    if dist[i] > 10:
        dist[i] = 'INF'
    print(dist[i])