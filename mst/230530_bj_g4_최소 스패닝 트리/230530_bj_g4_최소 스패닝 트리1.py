# 최소 스패닝 트리의 대표적인 두 가지 방식
# 크루스칼 알고리즘, 프림 알고리즘

# 프림 알고리즘은 다익스트라 알고리즘의 연장선
import sys
input = sys.stdin.readline

from collections import defaultdict
from heapq import heappush, heappop

def solution(V, E):
    answer = 0

    graph = defaultdict(list)
    for _ in range(E):
        A, B, C = map(int, input().split())
        graph[A].append((C, B))
        graph[B].append((C, A))

    visited = set()
    dist = [(0, 1)]
    while dist:
        c, d = heappop(dist)
        if d in visited:
            continue
        visited.add(d)
        answer += c
        for c, i in graph[d]:
            if i in visited:
                continue
            heappush(dist, (c, i))
    return answer

V, E = map(int, input().split())

print(solution(V, E))