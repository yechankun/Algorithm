def solution(maps):
    answer = 1
    maps_x_size = len(maps[0])
    maps_y_size = len(maps)
    visited = [[0]*maps_x_size for _ in range(maps_y_size)]
    visited[0][0] = 1
    direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = [(0,0)]
    while True:
        temp_q = []
        for xy in queue:
            for dx, dy in direct:
                next_x = xy[0] + dx
                next_y = xy[1] + dy
                if -1<next_x<maps_x_size and -1<next_y<maps_y_size and maps[next_y][next_x]:
                    if next_x == maps_x_size-1 and next_y == maps_y_size-1:
                        return answer + 1
                    if not visited[next_y][next_x]:
                        visited[next_y][next_x] = 1
                        temp_q.append((next_x,next_y))
        if not temp_q:
            return -1
        queue = temp_q
        answer += 1