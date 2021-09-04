def solution(rows, columns, queries):
    answer = []
    board = [[i+columns*j for i in range(1, columns+1)] for j in range(rows)]

    for q in queries:
        r1, c1, r2, c2 = (one-1 for one  in q)
        minN = temp = board[r1][c1]
        stack = [temp]
        for r in range(r1, r2):
            board[r][c1] = board[r+1][c1]
            stack.append(board[r][c1])

        for c in range(c1, c2):
            board[r2][c] = board[r2][c+1]
            stack.append(board[r2][c])

        for r in range(r2, r1, -1):
            board[r][c2] = board[r-1][c2]
            stack.append(board[r][c2])

        for c in range(c2, c1, -1):
            board[r1][c] = board[r1][c-1]
            stack.append(board[r1][c])
        answer.append(min(stack))
        board[r1][c1+1] = temp
    return answer