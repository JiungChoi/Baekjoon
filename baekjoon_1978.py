from sys import stdin
input()

cnt = 0
for i in list(map(int,stdin.readline().split())):
    if i ==2:
        cnt += 1
    elif i<2:
        continue
    else:
        for j in range(1, i//2 +1):
            if i%j==0:
                break
        else: cnt += 1
print(cnt)
