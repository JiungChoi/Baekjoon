ary = [-1 for _ in range(25)]
cnt = 0

for i in list(input()):
    if ary[ord(i)-97] == -1:
        ary[ord(i)-97] = cnt
    cnt += 1

print(ary)

