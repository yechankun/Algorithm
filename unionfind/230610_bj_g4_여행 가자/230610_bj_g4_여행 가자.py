import sys
input = sys.stdin.readline

def solution():        

    N = int(input())
    M = int(input())

    groups = {i:i for i in range(1, N+1)}

    def union(x, y):
        a = find(x)
        b = find(y)
        if b < a:
            a, b = b, a
        groups[b] = a
    
    def find(x):
        if groups[x] != x:
            return find(groups[x])
        return x

    for i in range(1, N+1):
        for j, conn in enumerate(map(int, input().split()), 1):
            if conn:
                union(i, j)
    check = list(map(int, input().split()))
    start = find(check[0])
    for i in check:
        if find(i) != start:
            return "NO"
    return "YES"

print(solution())