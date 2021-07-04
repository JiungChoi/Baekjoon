import sys

X, Y = map(int, sys.stdin.readline().split())
Z = int(100 * Y / X)
low, high = 0, 1000000000

if Z >=99: print(-1)
else:
    while low <= high:
        mid = (low + high) // 2
        if int(100 * (Y+mid)/(X+mid)) > Z: high = mid-1
        else: low = mid+1
    print(high+1)