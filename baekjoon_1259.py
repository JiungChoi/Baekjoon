from collections import deque

def say_yes_or_no(compare):

    cnt = len(compare) // 2
    compare = deque(compare)
    for _ in range(cnt):
        if compare.popleft() != compare.pop():
            return 'no'
    else: return 'yes'

while True:

    compare = list(input())
    if compare == ['0']:
        break
    else:
        print(say_yes_or_no(compare))
    

# from collections import deque
# 
# def say_yes_or_no():
#     compare = list(input())
#     compare = deque(compare)
#     while len(compare) > 1:
#         if compare.popleft() != compare.pop():
#             return 'no'
#     else: return 'yes'
# 
# for _ in range(int(input())):
#     print(say_yes_or_no())
