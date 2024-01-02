from collections import defaultdict

def solution(a, edges):
    answer = -2
    if sum(a) != 0:
        return -1
    
    # 그래프 만들기
    graph = defaultdict(list)
    # 간선 정보 입력
    for fr, to in edges:
        graph[fr].append(to)
        graph[to].append(fr)
        
    
    # 리프노드 찾기
    leaf = []
    for node in graph:
        if len(graph[node]) == 1:
            leaf.append(node)
    
    # 핵심부분 - 아쉽게 시간 내엔 틀린 부분
    conn_counts = [len(graph[i]) for i in range(len(a))]
    # leaf가 빌 때까지 반복
    visited = set()
    count = 0
    while leaf:
        nxt = []
        for l in leaf:
            if l in visited:
                continue
            visited.add(l)
            if a[l] == 0:
                continue
            for node in graph[l]:
                if node in visited:
                    continue
                a[node] += a[l]
                count += abs(a[l])
                a[l] = 0          
                conn_counts[node] -= 1
                if conn_counts[node] == 1:
                    nxt.append(node)
        leaf = nxt
    return count