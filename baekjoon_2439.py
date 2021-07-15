N = int(input())

star = '*'
space = ''
for _ in range(N-1):
    space = space + ' '

for i in range(N):
    print(space+star)
    space = space.replace(' ','',1)
    star = star + '*'