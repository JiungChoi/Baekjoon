import sys

cnt = 0
N, KIM, IM = map(int, sys.stdin.readline().split())

while KIM != IM:
    KIM -= KIM//2
    IM -= IM//2
    cnt += 1

print(cnt)