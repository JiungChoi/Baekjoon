unique_num = input().split()

hop = 0
for i in range(len(unique_num)):
    hop += int(unique_num[i]) ** 2

print(hop%10)