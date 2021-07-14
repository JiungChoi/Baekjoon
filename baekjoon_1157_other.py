s,a=input().lower(),[]
for i in range(97,123):
 a.append(s.count(chr(i)))
print('?'if a.count(max(a))>1 else chr(a.index(max(a))+97).upper())