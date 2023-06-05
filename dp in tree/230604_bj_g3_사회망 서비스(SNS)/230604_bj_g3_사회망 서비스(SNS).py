import sys
sys.stdin = open('dp in tree/230604_bj_g3_사회망 서비스(SNS)/3.in', "r")
input = sys.stdin.readline
from collections import defaultdict

def solution(n, graph, start):
    #n은 100만이다. 따라서 n^2는 불가능. O(nlogn, n)이 마지노선
    #dfs로 전체 탐색 = O(n)
    stack = [start]
    visited = [False] * (n+1)
    parent = defaultdict(int)
    dp = defaultdict(lambda: [0, 0])

    while stack:
        node = stack[-1]
        if not visited[node]:
            visited[node] = True
            for i in graph[node]:
                if not visited[i]:
                    parent[i] = node
                    stack.append(i)
        else:
            stack.pop()
            dp[node][1] += 1 + sum(min(dp[i]) for i in graph[node] if i != parent[node])
            dp[node][0] += sum(dp[i][1] for i in graph[node] if i != parent[node])
    return min(dp[start])

N = int(input())
graph = defaultdict(list)
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(solution(N, graph, 1))