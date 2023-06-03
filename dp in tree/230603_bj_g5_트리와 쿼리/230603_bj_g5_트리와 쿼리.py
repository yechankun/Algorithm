import sys
sys.setrecursionlimit(10**8)
# sys.stdin = open('dp/230603_bj_g5_트리와 쿼리/1.in', 'r')
input = sys.stdin.readline

from collections import defaultdict

def solution(n, tree, root, queries):
    dp = defaultdict(int) # query 결과를 임시저장할 dp
    # dp를 저장하기만 하면 쿼리당 시간복잡도는 O(1)이 된다.
    visited = [False] * (n+1)

    def dfs(tree, root):
        if visited[root]:
            return 0
        visited[root] = True
        dp[root] += 1
        for c_node in tree[root]:
            dp[root] += dfs(tree, c_node)
        return dp[root]
        
    dfs(tree, root)
    answer = []
    for query in queries:
        answer.append(dp[query])
    return answer

N, R, Q = map(int, input().split())

tree = defaultdict(list)
for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

queries = [int(input()) for _ in range(Q)]

print(*solution(N, tree, R, queries), sep='\n')