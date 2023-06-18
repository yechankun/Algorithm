import sys
# sys.stdin = open('bfs/230618_bj_s1_미로 탐색/1.in', 'r')

input = sys.stdin.readline

from collections import deque

def solution():
    N, M = map(int, input().split())

    board = [list(input()) for _ in range(N)]
    drc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(0, 0)])
    answer = 1
    while deque:
        answer += 1
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in drc:
                nr, nc = r + dr, c + dc
                if -1 < nr < N and -1 < nc < M and board[nr][nc] == '1':
                    if (nr, nc) == (N-1, M-1):
                        return answer
                    board[nr][nc] = '2'
                    queue.append((nr, nc))
    return answer

print(solution())