# https://school.programmers.co.kr/learn/courses/30/lessons/1843
# 풀이 알고리즘: dp

def solution(arr):
    # 최댓값과 최솟값을 갱신하면서 계산해야 된다.
    # 왜냐하면 -가 되면 최소값이 최대값이 되기 때문
    # 그렇게 되면 최소값과 최대값을 서로 교환한다.

    cmin, cmax = 0, 0  # 최소, 최대값
    psum, last = 0, 0
    for i in arr[::-1]:
        if i == "-":
            nmin = min(
                -(last + psum + cmax),
                -(last + psum) + cmin
            )
            nmax = max(
                -(last + psum + cmin),
                -(last) + psum + cmax
            )
            psum, last = 0, 0
            cmin, cmax = nmin, nmax
        elif i != '+':
            psum += last
            last = int(i)
    answer = psum + last + cmax
    return answer
