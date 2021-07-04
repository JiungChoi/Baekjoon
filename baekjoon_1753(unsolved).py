import sys

V, E = map(int,sys.stdin.readline().split())
K = int(input())

dist =['INF' for _ in range(V)]
dist[K-1] = 0
adj = [['INF' for _ in range(V)] for _ in range(V)]

# E개의 경로와 가중치
for i in range(E):
    u, v, w = map(int,sys.stdin.readline().split())
    adj[u-1][v-1] = str(w)

for i in range(V):
    dist[i] = min(dist[i],dist[K-1] + int(adj[K-1][i]))