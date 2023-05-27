# https://school.programmers.co.kr/learn/courses/30/lessons/161988
# 풀이 알고리즘: dp

# -1로 시작, 1로 시작 두 가지의 경우로 슬라이딩 윈도우?
# end를 늘리는 기준, max값보다 클 때 end를 늘린다?
# dp 문제에 가까워 보임.
#  1, 2, 3, 4, 5, 6 이란 배열이 있을 때
# 1 -2 3 -4 5 -6 이런 펄스로 계산
# 1 -1 3 -1 5 -6 = 5가 가장 큰 값이 됨

def solution(sequence):
    answer = 0
    minus = -1
    plus = 1
    # 0으로 시작할 경우, 1로 시작할 경우 두 경우로 나눔
    dp1 = [0] * (len(sequence) + 1)
    dp2 = [0] * (len(sequence) + 1)
    for i, s in enumerate(sequence, 1):
        dp1[i] = max(0, dp1[i-1]) + s * minus
        dp2[i] = max(0, dp2[i-1]) + s * plus
        # 펄스들의 부호를 반대로 바꿔줌
        minus = -minus
        plus = -plus
        # 최대값을 찾음
        answer = max(answer, dp1[i], dp2[i])
    return answer
