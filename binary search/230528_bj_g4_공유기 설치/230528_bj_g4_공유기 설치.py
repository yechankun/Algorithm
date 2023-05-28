import sys
input = sys.stdin.readline

N, C = map(int, input().split())
# X의 개수는 20만개, 정렬은 가능
x = [int(input().rstrip()) for _ in range(N)]
x.sort()

# 1, 2, 4, 8, 9
# 일단 가장 멀리 떨어뜨리기 위해서 처음은 8만큼 떨어지길 기대하자
# 그 다음은 4, 그 다음은 2, 그 다음은 3으로 이분 탐색
def solution(x, start, end) -> int:
    while start <= end:
        mid = (start+end)//2
        cnt, prev = 1, x[0]
        for i in range(1, N):
            if x[i] - prev >= mid:
                cnt += 1 # 공유기 설치
                prev = x[i]
        if cnt >= C: # 공유기가 너무 많이 설치된 경우
            start = mid + 1
        else: # 공유기가 너무 적게 설치된 경우
            end = mid - 1
    return start-1

print(solution(x, 1, x[-1]-x[0]))