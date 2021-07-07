from sys import stdin

cnt_answer = stdin.readline()
answer = input().split()
cnt_ask = int(stdin.readline())
ask = map(int, stdin.readline().split())

answer.sort()

for i in ask:
    start = 0
    end = int(cnt_answer) - 1

    while start != end:
        mid = (start + end) // 2
        if int(answer[mid]) == i:
            print(1)
            break
        elif int(answer[mid]) > i : end = mid - 1
        else : start = mid + 1
    else: print('1' if int(answer[start]) == i else '0')
