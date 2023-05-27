
# 정수 x에 사용할 수 있는 연산
# 3으로 나누어 떨어지면 3으로 나눔
# 2로 나누어 떨어지면 2로 나눔
# 1을 뺌

# 연산을 사용하는 횟수의 최솟값 구하기
# dp는 부분 문제를 풀어 전체 문제를 푸는 방식이다.

# 점화식 구하기
N = int(input())

# dp를 이용해서 정수 1부터 연산 횟수를 계산한다.
# 바텀 업 방식임.
dp = [0] * (N+1)
for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = dp[i//3] + 1
    elif i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
print(dp[N])

# # 탑 다운 형식으로 다시 풀기
# import sys
# sys.setrecursionlimit(10**8)
# N = int(input())
# dp = {1:0, 2:1, 3:1}

# def topdown(n):
#     if n in dp:
#         return dp[n]
#     if n % 3 == 0 and n % 2 == 0:
#         dp[n] = min(topdown(n//3)+1, topdown(n//2) + 1)
#     elif n % 3 == 0:
#         dp[n] = min(topdown(n-1) + 1, topdown(n//3) + 1)
#     elif n % 2 == 0:
#         dp[n] = min(topdown(n-1) + 1, topdown(n//2) + 1)
#     else:
#         dp[n] = topdown(n-1) + 1

#     return dp[n]

# print(topdown(N))
