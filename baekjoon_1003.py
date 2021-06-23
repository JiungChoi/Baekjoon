
import sys
#
#def pibo(n):
#    if n == 1 :
#        return 0, 1
#    elif n == 0:
#        return 1, 0
#    else:
#        return (pibo(n-1)[0] + pibo(n-2)[0],pibo(n-1)[1] + pibo(n-2)[1])
#        
#T = int(sys.stdin.readline())
#for i in range(T):
#    print(pibo(int(sys.stdin.readline())))
#    

T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    zero = 1
    one = 0
    tmp = 0
    for _ in range(n):
        tmp = one
        one = one + zero
        zero = tmp
    print(zero, one)

