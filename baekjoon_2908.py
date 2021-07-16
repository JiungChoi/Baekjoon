from sys import stdin
A, B = map(str, stdin.readline().split())

A, B = list(A), list(B)
A.reverse(), B.reverse()

compare = ["".join(A) , "".join(B)]
print(max(compare))

