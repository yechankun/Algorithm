import sys
sys.stdin = open('./1.in', 'r')

input = sys.stdin.readline

from collections import defaultdict

def solution():
    N, Q = map(int, input().split())

    graph = defaultdict(list)
    
    for _ in range(N-1):
        p, q, r = map(int, input().split())
        graph[p].append((q, r))
        graph[q].append((p, r))

    for _ in range(Q):
        k, v = map(int, input().split())
        visited = set()

        queue = [(v, float('inf'))]        
        visited.add(v)
        answer = 0
        
        while queue:
            nqueue = []
            for q, r in queue:
                for node, gr in graph[q]:
                    if gr < k or node in visited:
                        continue
                    visited.add(node)
                    nr = min(r, gr)
                    nqueue.append((node, nr))
                    answer += 1
            queue = nqueue
        print(answer)
    return

solution()
