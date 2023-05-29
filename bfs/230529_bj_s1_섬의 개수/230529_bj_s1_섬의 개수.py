import sys
input = sys.stdin.readline

def solution(w, h, board):
    answer = 0
    # 8방 탐색
    drc = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1, 1),(1, 1)]

    for r in range(h):        
        for c in range(w):
            if board[r][c]:
                queue = [(r, c)]
                board[r][c] = 0
                while queue:
                    nqueue = []
                    for x, y in queue:
                        for dr, dc in drc:
                            nr, nc = x + dr, y + dc
                            if not (0<=nr<h and 0<=nc<w and board[nr][nc]):
                                continue
                            nqueue.append((nr,nc))
                            board[nr][nc] = 0
                    queue = nqueue
                answer += 1
    return answer

while (inp:= tuple(map(int, input().split()))) != (0, 0):
    w, h = inp
    board = [list(map(int, input().split())) for _ in range(h)]
    print(solution(w,h,board))