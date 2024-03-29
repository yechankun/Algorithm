import sys
sys.stdin = open('simulation/230808_ct_g3_바이러스 실험/2.in', 'r')

input = sys.stdin.readline

def solution():
    n, m, k = map(int, input().split())

    board = [[5]*(n+1) for _ in range(n+1)]

    plus = [[0]*(n+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

    virus = [list(map(int, input().split())) for _ in range(m)]
    virus = [(age, r, c) for r, c, age in virus]
    virus.sort() # 어린 바이러스부터 섭취


    drc = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1))
    for round in range(k):
        # 바이러스 칸에 있는 양분 섭취, 나이만큼 섭취
        # 여러 바이러스일 경우 나이 어린 바이러스부터
        # 양분 섭취시 나이 1 증가, 본인 나이만큼 섭취 못하면 죽음
        death = []
        survive_virus = []
        for age, r, c in virus:
            if board[r][c] < age:
                death.append((age, r, c))
                continue
            board[r][c] -= age
            survive_virus.append((age+1, r, c))

        # 섭취 끝낸 후 죽은 바이러스는 양분으로 변함, 죽은 나이를 2로 나눈 값이 양분 됨. 
        # 몫사용
        for age, r, c in death:
            board[r][c] += age//2

        # 바이러스 번식 진행, 나이 5 이상의 바이러스만 번식함
        # 8개의 칸에 나이 1인 바이러스 생김, 상하좌우
        new_virus = []
        for age, r, c in survive_virus:
            if age % 5 != 0:
                continue
            for dr, dc in drc:
                nr, nc = r + dr, c + dc

                if 0 < nr <= n and 0 < nc <= n:
                    new_virus.append((1, nr, nc))   
        virus = new_virus + survive_virus # 재정렬
            
        ## 주어진 양분에 따라 자리가 양분 회복
        for i in range(n+1):
            for j in range(n+1):
                board[i][j] += plus[i][j]

    return len(virus)

print(solution())