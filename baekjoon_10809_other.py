ary = list(input())

for i in range(97,123):
    if chr(i) in ary:
        print(ary.index(chr(i)), end=' ')
    else : print(-1, end=' ')
        


