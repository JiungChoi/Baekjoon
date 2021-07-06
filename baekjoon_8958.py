for J in range(int(input())):
    score = 1
    total_score = 0
    S = input()
    for i in range(len(S)):
        if S[i] == 'O':
            total_score += score
            score += 1
        else:
            score = 1    
    print(total_score)