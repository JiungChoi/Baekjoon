A = int(input())
B = int(input())
C = int(input())

for i in range(10):
    print((f'{A * B * C}'.count(f'{i}')))