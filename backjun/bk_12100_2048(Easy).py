n = int(input())
Board = [list(map(int, input().split())) for _ in range(n)]

def rotate(n, board):
    new_list = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_list[j][n-i-1] = board[i][j]
    return new_list

def left_join(one_line):
    new_list = [i for i in one_line if i!=0]    #0을 제외한 list저장
    for i in range(1, len(new_list)):
        if new_list[i-1] == new_list[i]: #왼쪽과 오른쪽이 같으면 왼쪽2배 오른쪽 0
            new_list[i-1] *= 2
            new_list[i] = 0
    new_list = [i for i in new_list if i!=0] #합쳐진 list를 왼쪽으로 붙이기 위해 0제외
    return new_list + [0]*(n-len(new_list))    #list길이만큼 오른쪽에 0추가

def dfs(n, board, cnt):
    result = max([max(i) for i in board])
    if cnt == 0:
        return result
    for i in range(4): #상 하 좌 우(마지막 B는 무시된다.
        joined_board = [left_join(i) for i in board]    #list한줄씩 변환한뒤 합침
        result = max(result, dfs(n, joined_board, cnt-1))
        if i==3: break
        board = rotate(n, board)
    return result

print(dfs(n, Board, 5))