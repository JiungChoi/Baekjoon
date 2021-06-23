N = int(input())
A = input().split()
B = input().split()
S = 0

A.sort(reverse = True)
for i in range(N):
    S += int(A[i])*int(sorted(B)[i])
print(S)


