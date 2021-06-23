
N = int(input())

dic = {}
valid = []
result =''

for i in range(N):
    pre_in = input()
    if pre_in[0:1] in dic.keys():
        dic[pre_in[0:1]] += 1
        if dic[pre_in[0:1]] == 5:
            valid += pre_in[0:1] 
    else:
        dic[pre_in[0:1]] = 1

if not valid:
    print('PREDAJA')
else:
    valid.sort()
    for i in range(len(valid)):
        result += valid[i] 
    print(result)