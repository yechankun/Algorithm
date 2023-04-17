# https://school.programmers.co.kr/learn/courses/30/lessons/43236
# 풀이 알고리즘: 이분탐색

def solution(distance, rocks, n):
    answer = 0
    # 돌을 정렬한다.
    rocks.sort()
    # 도착지점을 돌 리스트에 추가한다.
    rocks = rocks + [distance]

    # 이분탐색을 이용해 최솟값의 최대값을 구한다.
    start, end = 1, distance
    while start <= end:
        # mid는 현재 이분탐색의 기준이 되는 거리이다.
        mid = (start + end) // 2

        # 현재 기준 거리(mid)로 돌을 제거할 수 있는지 확인한다.
        del_cnt, prev = 0, 0
        for r in rocks:
            # 돌 제거 기준
            if r - prev < mid:
                # 돌을 제거한다.
                del_cnt += 1
            else:
                # 돌을 제거하지 않는다면 현재 돌을 기준으로 다음 돌과의 거리를 구한다.
                prev = r
        # 돌 제거를 너무 많이 한 경우
        if n < del_cnt:
            end = mid - 1
        else:  # 돌 제거를 너무 적게 한 경우
            answer = mid
            start = mid + 1

    return answer
