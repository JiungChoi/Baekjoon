from sys import stdin
N, X = map(int, stdin.readline().split())
A = input().split()

ary = []
for num in A:
    if int(num) < X:
        print(num, end =' ')

    