import sys
input = sys.stdin.readline

# 이 문제는 NlogN 복잡도로 풀 수 있을 것이다.
# 모든 원소를 탐색하면서 이분탐색으로 짝을 이룰 때 최대한 0에 가까운 값을 찾는다.
def solution(N, items:list):
    answers = items[:2]
    min_total = sum(answers)
    for i in range(N-1):
        start, end = i+1, N-1
        while start <= end:
            mid = (start+end)//2
            total = items[i] + items[mid]
            if abs(total) < abs(min_total):
                min_total = total
                answers = [items[i], items[mid]]
            if total == 0:
                return answers
            elif total > 0:
                end = mid - 1
            else:
                start = mid + 1
    return answers

N = int(input())
items = list(map(int, input().split()))
items.sort()

print(*solution(N, items), sep=' ')