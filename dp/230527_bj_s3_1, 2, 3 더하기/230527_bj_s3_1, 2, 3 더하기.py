# 1, 2, 3의 합으로 숫자를 나타내는 방법

dp = {1:1, 2:2, 3:4}

# 1+(3)
# 1+(1+1+1)
# 1+(1+2)
# 1+(2+1)

# 2+(1+1)
# 2+(2)

# 3+(1)

# 탑 다운으로 푼다
def topdown(n):
    if n in dp:
        return dp[n]
    if n > 3:
        dp[n] = topdown(n-3) + topdown(n-2) + topdown(n-1)
    return dp[n]

for t in range(int(input())):
    n = int(input())
    print(topdown(n))
