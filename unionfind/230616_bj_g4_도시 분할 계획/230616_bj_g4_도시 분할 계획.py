import sys
sys.stdin = open('unionfind/230616_bj_g4_도시 분할 계획/1.in', 'r')

input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())

    # 그래프
    graph = []
    for _ in range(M):
        fr, to, p = map(int, input().split())
        graph.append((p, fr, to))
    graph.sort()

    groups = {fr: fr for fr in range(1, N+1)}
    # 유니온
    def union(a, b):
        a = find(a)
        b = find(b)
        if a < b:
            a, b = b, a
        groups[a] = b

    #파인드
    def find(x):
        if groups[x] == x:
            return x
        groups[x] = find(groups[x])
        return groups[x]

    # 크루스칼 알고리즘
    answer = 0 # answer는 비용
    cnt = 2
    if N == 2:
        return 0
    for p, fr, to in graph:
        if find(fr) != find(to):
            cnt +=1
            answer += p
            union(fr, to)
        if cnt == N:
            break
        
    return answer


print(solution())