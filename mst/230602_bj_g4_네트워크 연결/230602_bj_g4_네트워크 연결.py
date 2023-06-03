import sys
input = sys.stdin.readline
from collections import defaultdict
from heapq import heappush, heappop

def solution(graph, start):
    answer = 0
    dist = defaultdict(lambda: float('inf')) # 기본값을 inf로 가지는 딕셔너리
    visited = set()
    queue = [(0, start)]
    dist[start] = 0

    while queue:
        c, n = heappop(queue) # 가장 짧은 허브 찾기
        if n in visited: # 이미 방문된 것 빼기
            continue
        visited.add(n) # 방문처리
        answer += c # 정답 계산
        # 방문을 포함하고 다음 후보들 갱신
        for conn, nc in graph[n]:
            if conn not in visited and nc < dist[conn]:
                heappush(queue, (nc, conn))
                dist[conn] = nc
    return answer

# 입력
N, M = int(input()), int(input())

graph = defaultdict(list)
start = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    start = a
    graph[a].append((b, c))
    graph[b].append((a, c))

# 정답
print(solution(graph, start))