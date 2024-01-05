from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)

def solution(a, edges):
    if sum(a) != 0:
        return -1
    
    # 그래프 만들기
    graph = defaultdict(list)
    # 간선 정보 입력
    for fr, to in edges:
        graph[fr].append(to)
        graph[to].append(fr)
    
    visited = [0] * len(a)
    answer = 0
    def dfs(curr):
        nonlocal answer
        visited[curr] = True
        for child in graph[curr]:
            if visited[child]:
                continue
            a[curr] += dfs(child)

        a[curr], val = 0, a[curr]
        answer += abs(val)
        
        return val
    dfs(0)
    
    return answer