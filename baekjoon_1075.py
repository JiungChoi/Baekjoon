import sys
input = sys.stdin.readline

N = int(input())
F = int(input())

N2 = N % 100
N = N-N2

i= 0
while True:
    if (N+i)%F == 0:
        print(f'{str(N+i)[-2:]}')
        break
    i += 1

