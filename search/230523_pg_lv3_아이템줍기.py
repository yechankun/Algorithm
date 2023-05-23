# https://school.programmers.co.kr/learn/courses/30/lessons/87694

# 최단경로 문제, BFS로 풀 수 있을듯
# 1~50(2500개)까지의 좌표를 해야하나 2배로 해상도를 높여야함.
def solution(rectangle, characterX, characterY, itemX, itemY):
    # 1. 보드 초기화 51*51 사각형 -> 102*102 사각형
    # 내부는 1 외부는 0으로 한다.
    board = [[0]*102 for _ in range(102)]
    for rect in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, rect)
        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                board[y][x] = 1
    # 4방탐색
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dxy8 = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    # bfs 수행
    # 시작점은 2배로 해상도를 높인 좌표로 한다.
    queue = [(characterX*2, characterY*2)]
    goal = (itemX*2, itemY*2)
    answer = 0
    while queue:
        nqueue = []
        for pos in queue:
            if pos == goal:
                break
            x, y = pos
            for dx, dy in dxy:
                nx, ny = x+dx,y+dy
                # 갈 수 있는 위치면 8방 탐색을 통해 테두리인지 확인한다.
                if board[ny][nx] == 1:
                    for dx8, dy8 in dxy8:
                        cx, cy = nx+dx8, ny+dy8
                        if board[cy][cx] == 0:
                            nqueue.append((nx+dx, ny+dy))
                            board[ny][nx] = -1
                            board[ny+dy][nx+dx] = -1
        else:    
            queue = nqueue
            answer += 1
            continue
        break
    return answer