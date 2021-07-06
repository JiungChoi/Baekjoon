ary = input().split()

cnt = 0
for i in range(7):
    if ary[i] < ary[i+1]:
        cnt += 1
    elif ary[i] > ary[i+1]:
        cnt -= 1
else:
    print('ascending' if cnt == 7 else('descending' if cnt == -7 else 'mixed'))