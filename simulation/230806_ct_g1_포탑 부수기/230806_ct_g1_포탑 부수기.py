import sys
sys.stdin = open('simulation/230806_ct_g1_포탑 부수기/3.in', 'r')

input = sys.stdin.readline

from heapq import heappush

def solution():
    N, M, K = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]
    attacked = [[0] * M for _ in range(N)]

    def search(param):
        # param 1은 가장 약한 것, -1은 가장 강한 것
        candi = []
        for i in range(N):
            for j in range(M):
                param * board[i][j]
                if (not candi or param * board[i][j] <= candi[0][0]) and board[i][j] > 0:
                    heappush(candi, (param * board[i][j], -param * attacked[i][j], -param*(i+j), -param*j, i))
        if not candi:
            return 0,0,0,0,0
        return param * candi[0][0], -param*candi[0][1], -param*candi[0][2], -param*candi[0][3], candi[0][4]

    razer_drc = ((0, 1), (1, 0), (0, -1), (-1, 0))
    def razer_attack(a_r, a_c, b_r, b_c):
        queue = [[a_r, a_c, []]]
        visited = {(a_r, a_c)}
        while queue:
            nqueue = []
            for a_r, a_c, root in queue:
                for dr, dc in razer_drc:
                    nr, nc = (a_r + dr) % N, (a_c + dc) % M
                    if (nr, nc) not in visited and board[nr][nc] > 0:
                        nqueue.append((nr, nc, root + [(nr, nc)]))
                        visited.add((nr, nc))
                        if nr == b_r and nc == b_c:
                            return root+[(nr, nc)]
            queue = nqueue
        return False
    
    cannon_drc = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    def cannon_attack(a_r, a_c, b_r, b_c):
        root = []
        for dr, dc in cannon_drc:
            nr, nc = (b_r + dr) % N, (b_c + dc) % M
            if (nr == a_r and nc == a_c) or board[nr][nc] <= 0:
                continue
            root.append((nr, nc))
        return root + [(b_r, b_c)]
    
    def damage(dmg, root):
        for r, c in root:
            board[r][c] = max(0, board[r][c] - dmg)
        return
    
    def recover(root):
        check = set(root)
        for i in range(N):
            for j in range(M):
                if (i, j) not in check and board[i][j] > 0:
                    board[i][j] += 1
        return

    for i in range(1, K+1):
        a_health, _, _, a_c, a_r = search(1)
        b_health, _, _, b_c, b_r = search(-1)

        if a_r == b_r and a_c == b_c:
            return a_health
        
        root = razer_attack(a_r, a_c, b_r, b_c)
        attacked[a_r][a_c] = i

        if not root:
            root = cannon_attack(a_r, a_c, b_r, b_c)
        

        board[a_r][a_c] = dmg = a_health + N + M

        target = root[-1]

        damage(dmg, [target])
        damage(dmg//2, root[:-1]) # 나머지에 데미지 주기

        recover(root+[(a_r, a_c)])   

    return search(-1)[0]

print(solution())