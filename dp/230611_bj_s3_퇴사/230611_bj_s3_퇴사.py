import sys
input = sys.stdin.readline

def solution():
    N = int(input()) # N개의 상담이 있다
    TP = [list(map(int, input().split())) for _ in range(N)] # TP는 N개의 상담 T와 P로 이루어짐

    dp = [0] * (N+1)

    for i in range(N): # N날까지 반복
        for j in range(i+TP[i][0], N + 1): #
            # i+TP의 i번째 날부터 N날까지 더 많은 보수를 받으면 dp를 모두 갱신
            if dp[j] < TP[i][1] + dp[i]:
                dp[j] = TP[i][1] + dp[i]
    return dp[-1] # 최종 가장 큰 금액

print(solution())