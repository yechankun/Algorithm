import sys
sys.stdin = open('simulation/230809_ct_g5_놀이기구 탑승/1.in', 'r')

input = sys.stdin.readline

from heapq import heappush

def solution():
    n = int(input())

    # 학생 딕셔너리
    students = {}
    for _ in range(n*n):
        n0, n1, n2, n3, n4= map(int, input().split())
        students[n0] = {n1, n2, n3, n4}   
    

    board = [[0] * n for _ in range(n)]

    drc = ((-1,0),(1,0),(0,-1),(0,1)) # 상하좌우
    for s in students:
        candi = []
        
        for r in range(n):
            for c in range(n):
                if board[r][c]:
                    continue
                likes = 0
                empties = 0
                for dr, dc in drc:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < n and 0 <= nc < n:
                        if board[nr][nc] in students[s]:
                            likes += 1
                        elif not board[nr][nc]:
                            empties += 1
                heappush(candi, (-likes, -empties, r, c))
        _, _, r, c = candi[0]
        board[r][c] = s

    score_board = [0,1,10,100,1000]
    score = 0
    
    for r in range(n):
        for c in range(n):
            likes = 0
            s = board[r][c]
            for dr, dc in drc:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and board[nr][nc] in students[s]:
                    likes += 1
            score += score_board[likes]

    return score

print(solution())