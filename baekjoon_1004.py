import sys

T = int(sys.stdin.readline())
for _ in range(T):
    cnt = 0
    x1, y1, x2, y2 = map(int,sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    for _ in range(n):
        cx, cy, r = map(int,sys.stdin.readline().split())
        if r >= ((cx-x1)**2 + (cy-y1)**2)**(1/2) and r >= ((cx-x2)**2 + (cy-y2)**2)**(1/2):
            pass
        elif r >= ((cx-x1)**2 + (cy-y1)**2)**(1/2) or r >= ((cx-x2)**2 + (cy-y2)**2)**(1/2):
            cnt += 1
        
    print(f'{cnt}')
