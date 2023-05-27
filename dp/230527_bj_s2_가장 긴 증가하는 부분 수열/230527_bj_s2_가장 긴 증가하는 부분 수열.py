import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# 10 20 10 13 30 15 20 30
# # 1000*1000 = 1000000 번 수행

# 2차원 배열 혹은 저장할 무언가 필요
# 1, 2, 1, 2, 3

dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))