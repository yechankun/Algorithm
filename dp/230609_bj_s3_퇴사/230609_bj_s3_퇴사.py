import sys
sys.stdin = open('dp/230609_bj_s3_퇴사/1.in', 'r')
input = sys.stdin.readline

def solution():
    N = int(input())
    TP = [list(map(int, input().split())) for _ in range(N)]

    dp = [0] * (N+1)

    for i in range(N):
        for j in range(i+TP[i][0], N + 1):
            if dp[j] < TP[i][1] + dp[i]:
                dp[j] = TP[i][1] + dp[i]
    return dp[-1]

print(solution())
    