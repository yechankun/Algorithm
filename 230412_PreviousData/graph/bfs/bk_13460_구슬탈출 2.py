def move(board, x, y, dx, dy):
    move_cnt = 0 #움직인 거리
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O' :
        x+=dx
        y+=dy
        move_cnt += 1

    return x,y,move_cnt


row, col = map(int, input().split())

board = [list(input()) for _ in range(row)]

xy_directs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

for i in range(row):
    for j in range(col):
        if board[i][j] == 'R':
            red_x, red_y = i, j
        if board[i][j] == 'B':
            blue_x, blue_y = i, j

visited_set = set([(red_x, red_y, blue_x, blue_y)])
queue = [[(red_x, red_y, blue_x, blue_y)],[]]

attempt_cnt = 0
while (queue[0] or queue[1]) and attempt_cnt < 10:
    #print("현재 cnt:", attempt_cnt, "////////// 값", queue)
    #print("set", visited_set)
    red_x, red_y, blue_x, blue_y = queue[attempt_cnt%2].pop(0)

    for xy_direct in xy_directs:
        new_red_x, new_red_y, red_move_cnt = move(board, red_x, red_y, *xy_direct)
        new_blue_x, new_blue_y, blue_move_cnt = move(board, blue_x, blue_y, *xy_direct)

        if board[new_blue_x][new_blue_y] == 'O' :
            continue
        if board[new_red_x][new_red_y] == 'O':
            print(attempt_cnt+1)
            break

        if (new_red_x, new_red_y) == (new_blue_x, new_blue_y):
            if red_move_cnt > blue_move_cnt:
                new_red_x -= xy_direct[0]
                new_red_y -= xy_direct[1]
            else:
                new_blue_x -= xy_direct[0]
                new_blue_y -= xy_direct[1]

        if not (new_red_x, new_red_y, new_blue_x, new_blue_y) in visited_set :
            visited_set.add((new_red_x, new_red_y, new_blue_x, new_blue_y))
            queue[(attempt_cnt+1)%2].append((new_red_x, new_red_y, new_blue_x, new_blue_y))
    else:
        if not queue[attempt_cnt%2]:
            attempt_cnt+=1
        continue
    break
else:
    print(-1)


