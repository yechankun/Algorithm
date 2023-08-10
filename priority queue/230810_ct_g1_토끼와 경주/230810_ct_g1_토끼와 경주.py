import sys
sys.stdin = open('priority queue/230810_ct_g1_토끼와 경주/1.in', 'r')
input = sys.stdin.readline

from heapq import heappush, heappop, heapify

def solution():


    # 경주 시작 준비
    Q = int(input())

    _, N, M, P, *pids = list(map(int, input().split()))
    rabbits = list(zip(pids[::2], pids[1::2]))
    move_power = {}
    scores = {}
    for i in range(0, len(pids), 2):
        move_power[pids[i]] = pids[i+1]
        scores[pids[i]] = 0

    positions = [(0, 2, 1, 1, pid) for pid, d in rabbits]
    heapify(positions)
    add = 0


    positions = [(0, 2, 1, 1, pid) for pid, d in rabbits]
    heapify(positions)
    add = 0
    N2 = N*2-2
    M2 = M*2-2

    drc = ((-1, 0), (1, 0), (0, -1), (0, 1))
    # 경주 진행
    def start(K, S):
        nonlocal add
        winner = []
        for _ in range(K):
            cnt, s, r, c, pid = heappop(positions)
            nxt = []
            for dr, dc in drc:
                nr, nc = r + (dr*move_power[pid])%N2, c + (dc*move_power[pid])%M2

                # 이동
                while not (0 < nr <= N and 0 < nc <= M):
                    if nr < 1:
                        nr = -nr + 2
                    elif nr > N:
                        nr = N - (nr - N)
                    elif nc < 1:
                        nc = -nc + 2
                    elif nc > M:
                        nc = M - (nc - M)
                else:
                    heappush(nxt, (-(nr+nc), -nr, -nc ))           
            s, nr, nc = nxt[0]
            winner.append((-s, -nr, -nc, pid))

            # 나머지 토끼 점수 계산
            add += -s
            scores[pid] += s # 점수 빼버리기
            heappush(positions, (cnt+1, -s, -nr, -nc, pid)) # 최소값
        _, _, _, pid = max(winner)
        scores[pid] += S
        return
    
    # 이동 거리 변경
    def edit(pid_t, L):
        move_power[pid_t] *= L
        return

    commands = {200: start, 300: edit}

    # 명령 정보 받기
    for _ in range(Q-1):
        inputs = list(map(int, input().split()))
        if(inputs[0] == 400):
            break

        cmd, p1, p2 = inputs
        commands[cmd](p1, p2)

    return max(scores.values()) + add

print(solution())