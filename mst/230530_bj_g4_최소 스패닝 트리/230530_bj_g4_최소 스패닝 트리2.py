from collections.abc import MutableMapping
class HeapDict(MutableMapping):
    def __init__(self, *args, **kw):
        self.heap = []
        self.dict = {}
        self.update(*args, **kw)

    def clear(self):
        self.heap.clear()
        self.dict.clear()

    def __setitem__(self, key, value):
        if key in self.dict:
            self.pop(key)
        node = [value, key, len(self.heap)]
        self.dict[key] = node
        self.heap.append(node)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i):
        while i:
            parent = (i - 1) >> 1
            if self.heap[parent][0] < self.heap[i][0]:
                break
            if not self._swap(i, parent):
                break
            i = parent

    def _swap(self, i, j):
        if i == j:
            return False
        heap = self.heap
        heap[i], heap[j] = heap[j], heap[i]
        heap[i][2], heap[j][2] = i, j
        return True

    def _heapify_down(self, i):
        n = len(self.heap)
        heap = self.heap
        while True:
            smallest = i
            left = (i << 1) + 1
            right = (i + 1) << 1
            if left < n and heap[left][0] < heap[i][0]:
                smallest = left
            if right < n and heap[right][0] < heap[smallest][0]:
                smallest = right
            if not self._swap(i, smallest):
                break
            i = smallest

    def __delitem__(self, key):
        node = self.dict[key]
        while node[2]:
            # calculate the offset of the parent
            parentpos = (node[2] - 1) >> 1
            parent = self.heap[parentpos]
            self._swap(node[2], parent[2])
        self.popitem()

    def __getitem__(self, key):
        return self.dict[key][0]

    def __iter__(self):
        return iter(self.dict)

    def popitem(self):
        if len(self.heap) == 1:
            node = self.heap.pop()
        else:
            node = self.heap[0]
            self.heap[0] = self.heap.pop()
            self.heap[0][2] = 0
            self._heapify_down(0)
        value, key, _ = node
        del self.dict[key]
        return key, value

    def __len__(self):
        return len(self.dict)

    def peekitem(self):
        value, key, _ = self.heap[0]
        return key, value

import sys
# sys.stdin = open("mst/230530_bj_g4_최소 스패닝 트리/1.in", "r")
input = sys.stdin.readline

from collections import defaultdict

def solution(graph):
    answer = 0
    dist = HeapDict({i: float('inf') for i in graph})
    dist[1] = 0
        
    while dist:
        d, c = dist.popitem()
        answer += c
        for c, i in graph[d]:
            if i in dist and dist[i] > c:
                dist[i] = c
    return answer

V, E = map(int, input().split())
graph = defaultdict(list)
for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A].append((C, B))
    graph[B].append((C, A))

print(solution(graph))