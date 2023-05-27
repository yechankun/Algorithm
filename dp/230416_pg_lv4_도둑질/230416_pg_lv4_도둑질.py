# https://school.programmers.co.kr/learn/courses/30/lessons/42897
# 풀이 알고리즘: DP

def solution(money):
    # 첫번째 집을 터는 경우와 마지막 집을 터는 경우를 나눠서 dp를 구성한다.
    reverse = money[::-1]
    # dp1: 첫번째 집을 터는 경우
    dp1 = [0] * len(money)
    # dp2: 마지막 집을 터는 경우
    dp2 = [0] * len(money)
    dp1[0], dp2[0] = money[0], reverse[0]
    answer = max(money)
    # dp1, dp2를 순회하며 각각의 경우의 수를 구한다.
    for i in range(1, len(money)-1):
        # i번째 집을 터는 경우는 i-1번째 집을 터는 경우와 i-2번째 집을 터는 경우 중 큰 값을 선택한다.
        dp1[i] = max(dp1[i-1], money[i]+dp1[i-2])
        dp2[i] = max(dp2[i-1], reverse[i]+dp2[i-2])
        answer = max(answer, dp1[i], dp2[i])
    return answer
