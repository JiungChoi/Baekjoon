ary = []
for i in range(int(input())):
    pre_in = input()
    if [len(pre_in),pre_in] not in ary: ary.append([len(pre_in),pre_in])
ary.sort()

for i in ary:
    print(i[1])

