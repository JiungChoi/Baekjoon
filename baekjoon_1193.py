okay = 0
cnt, i = 1,1

X = int(input())
while not okay:
    if (cnt<=X) and ((cnt+i)>X):
            if i%2 == 1:
                print(f'{i-(X-cnt)}/{X-cnt+1}')
            else:
                print(f'{X-cnt+1}/{i-(X-cnt)}')
            okay = 1
    cnt += i
    i += 1
