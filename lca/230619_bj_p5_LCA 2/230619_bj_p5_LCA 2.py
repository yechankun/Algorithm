import sys

sys.stdin = open('lca/230619_bj_p5_LCA 2/1.in', 'r')
input = sys.stdin.readline

def solution():
    N = int(input())

    # 그래프 입력    
    graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)


    # 1부터 트리 재구성
    levels = [0] * (N+1)
    from math import ceil, log2
    # 높이는 2^h번째이므로 최대 부모 개수는 logN
    h = ceil(log2(N))+1
    dp = [[0] * h for _ in range(N+1)]
    
    def dfs(start):
        stack = [(start, 0, -1)]  # node, depth, parent
        while stack:
            node, depth, parent = stack.pop()
            levels[node] = depth
            dp[node][0] = parent
            for child in graph[node]:
                if child != parent:
                    stack.append((child, depth+1, node))

    dfs(1)

    # sparse table, 2^i 번째의 부모가 저장된다.
    for c in range(1, h):
        for p in range(1, N+1):
            dp[p][c] = dp[dp[p][c-1]][c-1]
    
    def LCA(x1, x2):
        # 작은 값을 a로 만들어주기(우리는 a의 높이를 높일 것이다)
        if levels[x1] < levels[x2]:
            x1, x2 = x2, x1
        a, b = levels[x1], levels[x2]
        
        # 같은 높이로 맞춰주기
        # 같은 높이로 맞추는 것은 이진 수를 이용해서 층을 높여간다.
        # 5 층 차이 = 101 = sparse 테이블 1칸 이동 후 2칸 이동
        for i in range(h-1, -1, -1):
            if levels[x1] - (1 << i) >= levels[x2]:
                x1 = dp[x1][i]

        if x1 == x2:
            return x1
        
        # 같은 부모가 될 때까지 양 부모를 한 칸씩 높여주기
        for i in range(h-1, -1, -1):
            if dp[x1][i] != dp[x2][i]:
                x1 = dp[x1][i]
                x2 = dp[x2][i]
        return dp[x1][0]

    outputs = []
    for _ in range(int(input())):
        a, b = map(int, input().split())
        outputs.append(str(LCA(a, b)))
    print('\n'.join(outputs))

    return
solution()