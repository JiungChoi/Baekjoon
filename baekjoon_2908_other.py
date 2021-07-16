
a, b =input().split()


a = a[::-1]
print(a)

def reading(k):
    k = k[::-1]
    return int(k)

print(max([reading(a),reading(b)]))

