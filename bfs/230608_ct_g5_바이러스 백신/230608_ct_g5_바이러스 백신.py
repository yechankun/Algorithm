import sys
# sys.stdin = open("bfs/230608_ct_g5_바이러스 백신/3.in", "r")

input = sys.stdin.readline

from itertools import combinations

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def solution(N, M, board):
    def find_obj(numbers):
        hpos = []
        virus = 0
        for r in range(N):
            for c in range(N):
                if numbers[r][c] == 2:
                    hpos.append((r, c))
                elif numbers[r][c] == 0:
                    virus += 1
        return hpos, virus
    
    def choose_hospital(hpos, M):
        return list(combinations(hpos, r = M))

    
    hpos, virus = find_obj(board)
    combpos = choose_hospital(hpos, M)
    drc = [(-1,0), (1,0), (0,-1), (0,1)]

    def bfs(hpos, board, virus, currmin):
        mintime = 0
        queue = hpos[:]
        visited = set(queue)

        while queue:
            if currmin < mintime:
                return currmin
            if virus <= 0:
                return mintime
            
            nqueue = []
            for r, c in queue:
                for dr, dc in drc:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited and board[nr][nc] != 1:
                        nqueue.append((nr, nc))
                        visited.add((nr,nc))
                        if board[nr][nc] == 0:
                            virus -= 1
            queue = nqueue
            mintime += 1
        return float('inf')
    
    answer = float('inf')
    for hpos in combpos:
        answer = min(answer, bfs(hpos, board, virus, answer))

    return answer if answer != float('inf') else -1

print(solution(N, M, board))