import sys


def selct(target, i, Button):
    tmp = ''
    tmp += target[0:i]
    tmp_up = tmp_down = target[i]
    
    while tmp_up in Button:
        tmp_up += 1
    tmp_up = tmp + str(tmp_up) + '00'
    while tmp_down in Button:
           tmp_down -= 1
    
Now = 100
target = input() ; direct = abs(Now - int(target))
target = list(target) ; target_l = len(target)
tmp =''
wrong= int(sys.stdin.readline())
Button =0
result = 0

if wrong:
    Button = list(map(int,sys.stdin.readline().split()))
    for i in range(target_l):
        if int(target[i]) in Button:
            result += selct(target, i, Button)
        else:
            tmp += str(target[i])
            result += 1

print(result)
print(type(result))