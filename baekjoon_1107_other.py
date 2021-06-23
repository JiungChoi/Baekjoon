N = int(input())
M = int(input())

remote_controller = {str(i) for i in range(10)}

if M:
    remote_controller -= set(map(str, input().split()))

now = 100
min_cnt = abs(now - N)
for channel in range(1000000):
    for j in range(len(str(channel))):
        if str(channel)[j] not in remote_controller:
            break
        elif len(str(channel)) -1 == j:
            min_cnt = min(min_cnt, abs(channel - N) + len(str(channel)))
print(min_cnt)