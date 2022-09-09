from collections import defaultdict
def solution(n, paths, gates, summits):
    summitsSet = set(summits)
    l = n + 1
    graph = defaultdict(list)
    dist = [10000001] * l
    
    for f, t, w in paths:
        graph[f].append((t, w))
        graph[t].append((f, w))

    for g in gates:
        dist[g] = 0
    gates = set(gates)

    while gates:
        for _ in range(len(gates)):
            node = gates.pop()
            for n, w in graph[node]:
                temp = max(w, dist[node])
                if dist[n] > temp:
                    dist[n] = temp
                    if n not in summitsSet:
                        gates.add(n)
    return min([[summit, dist[summit]] for summit in summits], key=lambda x: (x[1], x[0]))




print(solution(6,	[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],	[1, 3],	[5]))