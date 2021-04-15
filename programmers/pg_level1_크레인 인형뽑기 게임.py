def solution(board, moves):
    answer = 0
    basket = []
    tmp = 0
    for k in moves:
        for i in range(len(board)):
            if board[i][k-1] != 0:
                if basket:
                    tmp = basket.pop()
                    if tmp == board[i][k-1]:
                        board[i][k-1] = 0
                        answer+=2
                        break
                    basket.append(tmp)
                basket.append(board[i][k-1])
                board[i][k-1] = 0
                break
    return answer
