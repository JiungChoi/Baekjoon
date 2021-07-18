ary = set()
for _ in range(10):
    ary.update(str(int(input())%42))
print(len(ary))
print(ary)