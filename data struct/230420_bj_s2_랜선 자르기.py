# https://www.acmicpc.net/problem/1654
# 풀이 알고리즘: 이분탐색

import sys

K, N = map(int, sys.stdin.readline().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]

start = 1
end = max(lan)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for l in lan:
        cnt += l // mid
    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
