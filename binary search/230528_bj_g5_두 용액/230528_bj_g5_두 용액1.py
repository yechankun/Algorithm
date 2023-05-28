import sys
input = sys.stdin.readline

# 이 문제는 N 복잡도로 풀 수 있을 것이다.
# 모든 원소를 좌 우로 1칸씩 탐색하며 0에 가까운 값을 찾는다.
def solution(N, items:list):
    start, end = 0, N-1
    answers = []
    min_total = 10**9 * 2 + 1
    while start < end:
        total = items[start] + items[end]

        if abs(total) < abs(min_total):
            min_total = total
            answers = [items[start], items[end]]

        if total == 0:
            return answers
        elif total < 0:
            start += 1
        else:
            end -= 1
    return answers

N = int(input())
items = list(map(int, input().split()))
items.sort()

print(*solution(N, items), sep=' ')