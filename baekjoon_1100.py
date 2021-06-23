cnt = 0
for i in range(1,9):
    k = 1
    list = input()
    for j in list:
        if (i+k)%2 == 0:
            if j == 'F':
                cnt+=1
        k+=1

print(f'{cnt}')
