# https://www.acmicpc.net/problem/2252
# 풀이 알고리즘: 위상 정렬

import sys
input = sys.stdin.readline
n, m = map(int, input().split())

# 위상 정렬로 문제를 풀 수 있어 보인다.
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

# 진입 차수가 0인 것들을 큐에 넣는다.

q = []
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    next_q = []
    for now in q:
        print(now, end=' ')
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                next_q.append(i)
    q = next_q
