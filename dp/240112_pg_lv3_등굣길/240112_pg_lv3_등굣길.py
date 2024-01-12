# dp 문제
def solution(m, n, puddles):
    puddles_set = set()
    for r, c in puddles:
        puddles_set.add((c,r))
    board = [[0]*(m+1) for _ in range(n+1)]    
    for r in range(1, n+1):
        for c in range(1, m+1):
            if (r, c) in puddles_set:
                continue
            board[1][1] = 1
            board[r][c] = board[r-1][c]+board[r][c-1]
    return board[n][m] % 1000000007