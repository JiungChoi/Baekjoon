import sys

def count_num(start_board, board, N, M):
    cnt = 64
    for i1 in range(N-7):
        for i2 in range(M-7):
            pre_cnt = 0
            for i3 in range(8):
                for i4 in range(8):
                    if board[i1+i3][i2+i4] != start_board[i3][i4]:
                        pre_cnt += 1 
            if pre_cnt < cnt: cnt = pre_cnt
    return cnt

board_w =  [['W','B','W','B','W','B','W','B',],
            ['B','W','B','W','B','W','B','W',],
            ['W','B','W','B','W','B','W','B',],
            ['B','W','B','W','B','W','B','W',],
            ['W','B','W','B','W','B','W','B',],
            ['B','W','B','W','B','W','B','W',],
            ['W','B','W','B','W','B','W','B',],
            ['B','W','B','W','B','W','B','W',]]
board_b =  [['B','W','B','W','B','W','B','W',],
            ['W','B','W','B','W','B','W','B',],
            ['B','W','B','W','B','W','B','W',],
            ['W','B','W','B','W','B','W','B',],
            ['B','W','B','W','B','W','B','W',],
            ['W','B','W','B','W','B','W','B',],
            ['B','W','B','W','B','W','B','W',],
            ['W','B','W','B','W','B','W','B',]]            

N, M = map(int,sys.stdin.readline().split())
board = [list(input()) for _ in range(N)]
print(min(count_num(board_w, board, N, M),count_num(board_b, board, N, M)))


