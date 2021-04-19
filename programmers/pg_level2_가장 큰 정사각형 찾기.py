def solution(board):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if not board[i][j]:
                continue
            if not i or not j:
                answer = max(answer, board[i][j])
            else:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
                answer = max(answer, board[i][j])
    return answer * answer
