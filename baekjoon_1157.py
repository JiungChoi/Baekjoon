from sys import stdin

dic = {}

ary1 = list(stdin.readline())

for i in ary1:
    if  (122 >= ord(i) and (ord(i) >= 97):
        if f'{chr(ord(ary1[i])-32)}' in dic.keys:
            dic[f'{chr(ord(ary1[i])-32)}'] += 1
        else: dic[f'{chr(ord(ary1[i])-32)}'] = 1
    else:
        if ary1[i] in dic.keys:
            dic[ary1[i]] += 1
        else: dic[ary1[i]] = 1
