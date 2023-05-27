# https://school.programmers.co.kr/learn/courses/30/lessons/42898
# 풀이 알고리즘: dp

def solution(m, n, puddles):
    # 오른쪽, 아래로 이동하며 등굣길의 갈 수 있는 경우의 수를 구하는 문제이므로
    # 임의의 첫번째 열, 행을 0으로 추가하여 dp를 구성한다.
    # 1행, 1열은 1로 초기화한다.
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1
    # 웅덩이가 있는 곳은 set을 이용해 관리한다. 웅덩이는 열, 행 번호로 저장된다
    puddles_set = set(map(tuple, puddles))
    # dp를 순회한다.
    for r in range(1, n+1):
        for c in range(1, m+1):
            # 웅덩이가 있는 곳은 건너뛴다.
            if (c, r) in puddles_set:
                continue
            # r,c로 도달하는 경우의 수는 r-1,c와 r,c-1로 도달하는 경우의 수의 합이다.
            dp[r][c] += dp[r-1][c] + dp[r][c-1]
    # dp[n][m]이 등굣길의 경우의 수이다. 1000000007로 나눈 나머지를 반환한다.
    return dp[n][m] % 1000000007
