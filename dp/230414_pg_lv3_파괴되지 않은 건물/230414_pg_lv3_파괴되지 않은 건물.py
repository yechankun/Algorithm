# https://school.programmers.co.kr/learn/courses/30/lessons/92344
# 풀이 알고리즘: 누적합(dp의 일종), 구현

# 2차원 누적합을 이용해 해결
# 1차원 0~3까지 범위 1증가를 누적합으로 표현하면 1, 0, 0, 0, -1 이 된다.
def solution(board, skill):
    answer = 0

    R = len(board)
    C = len(board[0])
    # 누적합으로 영향을 표현하려면 한 칸이 더 필요하다.
    pre_sum = [[0] * (C+1) for _ in range(R+1)]

    def update(type, r1, c1, r2, c2, degree):
        pm = {1: -1, 2: 1}
        # 누적합이 계산될 때는 위에서 아래로, 왼쪽에서 오른쪽으로 계산되게 된다.
        effect = [(r1, c1, 1), (r1, c2+1, -1), (r2+1, c1, -1), (r2+1, c2+1, 1)]
        for r, c, b in effect:
            pre_sum[r][c] += degree * b * pm[type]

    for s in skill:
        update(*s)

    # 2차원 누적합 결과 구하기
    for r in range(R):
        for c in range(C):
            pre_sum[r+1][c] += pre_sum[r][c]

    for r in range(R):
        for c in range(C):
            pre_sum[r][c+1] += pre_sum[r][c]
            if board[r][c] + pre_sum[r][c] > 0:
                answer += 1
    return answer
