import sys
sys.stdin = open("simulation/230807_ct_g2_싸움땅/3.in", "r")

input = sys.stdin.readline

from heapq import heappush, heappop

def solution():
    n, m, k = map(int, input().split())
    ground_guns = [[[] for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        powers = list(map(int, input().split()))
        for j in range(1, n+1):
            heappush(ground_guns[i][j], -powers[j-1])

    players = [[0,0,0,0,0]] + [list(map(int, input().split())) + [0] for _ in range(m)]
    positions = [[0]*(n+1) for _ in range(n+1)]
    for i, p in enumerate(players):
        x, y, _, _, _ = p
        positions[x][y] = i
    scores = [0] * (m+1)

    def get_gun(id):
        x, y, d, s, w = players[id]
        # 가지고 있는 무기보다 떨어져 있는 가장 쎈 무기가 더 쎌 경우
        if w < -ground_guns[x][y][0]:
            heappush(ground_guns[x][y], -w)
            w = -heappop(ground_guns[x][y])       
        players[id] = x, y, d, s, w
    
    def fight(id1, id2):
        x1, y1, d1, s1, w1 = players[id1]
        x2, y2, d2, s2, w2 = players[id2]

        winner, loser = id1, id2
        if s1 + w1 < s2 + w2:
            winner, loser = loser, winner
        elif s1 + w1 == s2 + w2 and s1 < s2:
            winner, loser = loser, winner
        return winner, loser, abs(s1 + w1 - s2 - w2)
    
    def player_check(x, y):
        return positions[x][y]
    
    def loser_move(id):
        x, y, d, s, w = players[id]

        # 총 내려 놓기
        heappush(ground_guns[x][y], -w)

        # 새로운 위치로 이동
        dx, dy = dxy[d]
        nx, ny = x + dx, y + dy
        # 격자 밖이거나 사람 있을 경우 90도 회전
        while not (0 < nx <= n and 0 < ny <= n) or player_check(nx, ny):
            d = (d + 1) % 4
            dx, dy = dxy[d]
            nx, ny = x + dx, y + dy
        positions[nx][ny] = id
        players[id] = nx, ny, d, s, 0

    dxy = ((-1, 0), (0, 1), (1, 0), (0, -1))
    def move(id):
        x, y, d, s, w = players[id]
        dx, dy = dxy[d]
        nx, ny = x + dx, y + dy
        if not (0 < nx <= n and 0 < ny <= n):
            d = (d + 2) % 4
            dx, dy = dxy[d]
            nx, ny = x + dx, y + dy
        positions[x][y] = 0 # 기존 위치 초기화
        players[id] = nx, ny, d, s, w

    for round in range(k):
        for id in range(1, m+1):     
            # 향하고 있는 방향 1칸 이동, 격자 벗어나면 반대로 1칸 이동
            move(id)

            x, y, _, _, _ = players[id]

            # 플레이어 있으면 두 플레이어 싸우기, 초기능력치+총 공격력 합으로 이긴 플레이어가 승리, 이긴 플레이어는 포인트 획득
            id2 = player_check(x, y)
            if id2:
                winner_id, loser_id, point = fight(id, id2)
                # 패자는  총 내려 놓기, 원래 방향으로 한 칸 이동, 다른 플레이어나 범위 밖인 경우 90도로 꺾어서 이동할 수 있을 때까지 이동
                # 이동한 곳에서 총 획득
                loser_move(loser_id)
                get_gun(loser_id)
                # 이긴 플레이어는 총 있는지 확인 후 획득, 이미 있으면 더 쎈거 획득 및 나머지 내려 놓기
                get_gun(winner_id)
                # 승자 위치 확정
                positions[x][y] = winner_id
                # 승자 점수 획득
                scores[winner_id] += point
            else:
                # 이동 위치에 플레이어 없으면 총 있는지 확인 후 획득, 이미 있으면 더 쎈거 획득 및 나머지 내려 놓기
                get_gun(id)
                # 아이디 갱신
                positions[x][y] = id
    return scores[1:]

print(*solution())