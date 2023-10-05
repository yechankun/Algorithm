import sys

sys.stdin = open('simulation/231004_ct_g3_예술성/1.in', 'r')

input = sys.stdin.readline

from collections import defaultdict
def solution():
    n = int(input())

    board = [list(map(int, input().split())) for _ in range(n)]


    # 예술점수 평가
    def eval():
        group = [[0] * n for _ in range(n)]

        # 전체 반복하며 그룹 번호 매기기
        group_n = 1
        drc = ((-1, 0), (1, 0), (0, -1), (0, 1))
        group_cnt = defaultdict(int)
        group_real = defaultdict(int)
        sides = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if group[i][j] != 0:
                    continue
                queue = [(i, j)]
                group[i][j] = group_n # 그룹번호
                group_real[group_n] = board[i][j] # 그룹번호 실제번호 매핑
                group_cnt[group_n] += 1
                while queue:
                    nqueue = []
                    for r, c in queue:
                        for dr, dc in drc:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < n and 0 <= nc < n and group[nr][nc] == 0:
                                if board[nr][nc] == board[r][c]:
                                    nqueue.append((nr, nc))
                                    group[nr][nc] = group_n # 그룹번호
                                    group_cnt[group_n] += 1
                                else:
                                    sides[group_n].append((nr, nc))
                    queue = nqueue
                group_n += 1  # 그룹 번호 1 추가
        score = 0
        for group_an in sides:
            side_groups = defaultdict(int)
            for r, c in sides[group_an]:
                side_groups[group[r][c]] += 1
            # 모서리가 겹치는 모든 그룹 점수 계산
            for group_bn in side_groups:
                a_cnt, b_cnt = group_cnt[group_an], group_cnt[group_bn]
                a_num, b_num = group_real[group_an], group_real[group_bn]
                
                # (그룹 a에 속한 칸의 수 + 그룹 b에 속한 칸의 수 ) x 그룹 a를 이루고 있는 숫자 값 x 그룹 b를 이루고 있는 숫자 값 x 그룹 a와 그룹 b가 서로 맞닿아 있는 변의 수
                score += (a_cnt + b_cnt) * a_num * b_num * side_groups[group_bn]
        return score
    
    def rotation():
        temp = [[board[r][c] for c in range(n)] for r in range(n)]
        half_n = n//2
        for r in range(n):
            for c in range(n):
                if r == half_n or c == half_n:
                    board[r][c] = temp[c][n-r-1]

        origin_rc = ((0,0), (0, half_n+1), (half_n+1, 0), (half_n+1, half_n+1))
        temp = [[board[r][c] for c in range(n)] for r in range(n)]
        for ori_r, ori_c in origin_rc:
            for r in range(half_n):
                for c in range(half_n):
                    board[ori_r+r][ori_c+c] = temp[ori_r+half_n-c-1][ori_c+r]
        
        return
    
    answer = eval() #초기 예술 점수
    for _ in range(3):
        rotation()
        answer += eval()
    return answer

print(solution())