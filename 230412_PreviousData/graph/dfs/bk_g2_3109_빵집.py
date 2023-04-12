#백트래킹과 그리디
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
load = [list(input()) for _ in range(R)]
    
count = 0
LC = C - 1
dr = [-1,0,1]

def dfs(row, col):
    for i in dr:
        nr = row + i
        nc = col + 1
        if nr > -1 and nr < R and load[nr][nc] == '.':
            if nc == LC:
                return True
            load[nr][nc] = 'V'
            if dfs(nr, nc):
                return True
    return False

            
for i in range(R):
    if dfs(i, 0):
        count += 1
print(count)

    
