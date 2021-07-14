from sys import stdin

dic = {}
ary1 = list(stdin.readline())

for i in ary1:
    if  (122 >= ord(i)) and (ord(i) >= 97):
        if chr(ord(i)-32) in dic:
            dic[chr(ord(i)-32)] += 1
        else: dic[chr(ord(i)-32)] = 1
    elif i != '\n':
        if i in dic:
            dic[i] += 1
        else: dic[i] = 1
    else: pass

cnt = 0
for v in dic.values():
    if cnt < v:
        cnt = v

n_cnt = 0
for k,v in dic.items():
    if v == cnt:
        n_cnt += 1
        if n_cnt > 1:
            print('?')
            break
else: 
    for k,v in dic.items():
        if v == cnt:
            print(k)
