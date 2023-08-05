## 문제 링크

[15591번: MooTube (Silver)](https://www.acmicpc.net/problem/15591)

## 문제 풀이

1. BFS로 푼다.
2. 큐를 이용해서 탈출 조건(이미 방문 or K 이상)이 되면 큐에 넣지 않는 방식으로 순회한다.
3. 방문할 때마다 answer를 1씩 증가시킨다

## 풀이 코드

```python
import sys
# sys.stdin = open('./1.in', 'r')

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
```