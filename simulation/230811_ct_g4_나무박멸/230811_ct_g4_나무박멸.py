import sys

sys.stdin = open('simulation/230811_ct_g5_나무박멸/1.in')
input = sys.stdin.readline


def solution():
    # 초기화
    n, m, k, year = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(n)]
    # 벽을 마이너스 무한으로 만듬
    for r in range(n):
        for c in range(n):
            if board[r][c] < 0:
                board[r][c] = -float('inf')

    # 나무성장
    drc = ((-1,0),(1,0),(0,-1),(0,1))

    def grow():
        for r in range(n):
            for c in range(n):
                if board[r][c] > 0:
                    cnt = 0
                    for dr, dc in drc:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and board[nr][nc] > 0:                            
                            cnt += 1
                    board[r][c] += cnt                  
        return
    # 번식
    def breeding():
        copy = [list(board[r]) for r in range(n)] # 모든 나무 동시에 하기 위한 카피
        for r in range(n):
            for c in range(n):
                if copy[r][c] > 0:
                    cnt = 0
                    for dr, dc in drc: # 번식할 위치 파악
                        nr, nc = r + dr, c + dc 
                        if 0 <= nr < n and 0 <= nc < n and copy[nr][nc] == 0:                            
                            cnt += 1
                    if cnt == 0: # 번식할 곳 없으면 다음으로
                        continue
                    for dr, dc in drc: # 번식
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and copy[nr][nc] == 0:
                            board[nr][nc] += board[r][c] // cnt
        return

    drc2 = ((-1, -1), (-1, 1), (1, -1), (1, 1))
    def poison():
        # 나무 박멸
        
        candi = []

        for r in range(n):
            for c in range(n):
                if board[r][c] > 0:
                    cnt = board[r][c]
                    for dr, dc in drc2:
                        for add in range(1, k+1):
                            nr, nc = r + add*dr, c + add*dc
                            if 0 <= nr < n and 0 <= nc < n:
                                if board[nr][nc] <= 0:
                                    break
                                if board[nr][nc] > 0:
                                    cnt += board[nr][nc]
                    candi.append((cnt, -r, -c))

        if not candi:
            return 0
        
        cnt, r, c = max(candi)
        r, c = -r, -c # 부호 반대 되돌리기
        board[r][c] = -year - 1
        for dr, dc in drc2:
            for add in range(1, k+1):
                nr, nc = r + add*dr, c + add*dc

                if 0 <= nr < n and 0 <= nc < n:
                    if type(board[nr][nc]) is float:
                        break
                    if board[nr][nc] <= 0:
                        board[nr][nc] = -year - 1
                        break
                    elif board[nr][nc] > 0:
                        board[nr][nc] = -year - 1
        return cnt
    
    def next_year():
        for r in range(n):
            for c in range(n):
                if board[r][c] < 0:
                    board[r][c] += 1

    answer = 0
    for _ in range(m):
        grow()
        breeding()
        answer += poison()
        next_year()
    return answer


print(solution())
