from sys import stdin

N = input()
a = stdin.readline().split()


for i in range(int(N)):
    a[i] = int(a[i])

standard = max(a)
avr = 0
for i in range(int(N)):
    a[i] = (int(a[i]) / int(standard)) * 100
    avr += a[i]

print(avr/int(N))

    