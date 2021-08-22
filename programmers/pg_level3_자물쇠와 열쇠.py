# 끼워 맞춰보기
def attach(row, col, key_len, key_bits, board):
    count = 0
    for i in range(row, row+key_len):
        board[i] ^= key_bits[count] << col
        count += 1
# 원복
def detach(row, col, key_len, key_bits, board):
    count = 0
    for i in range(row, row+key_len):
        board[i] ^= key_bits[count] << col
        count += 1
# 비트마스크 90도 우측 회전
def rotate(key_len, key_bits):
    temp_key_bits = [0] * key_len
    count = 0
    for i in range(key_len-1, -1, -1):
        for j in range(key_len):
            temp_key_bits[i] |= (key_bits[j] & 1) << j
            key_bits[j] >>= 1
        count+=1
    return temp_key_bits

# 비트마스크로 자물쇠 열 수 있는지(홈이 다 채워졌는지) 체크
def isFull(lock_len, board):
    for i in range(lock_len):
        for j in range(lock_len):
            if(board[i+lock_len] & 1<<lock_len<<j == 0):
                return False
    return True

def solution(key, lock):
    answer = True
    key_len = len(key)
    key_bits = [0]*key_len
    # 비트마스크 key 리스트
    for i in range(key_len):
        for j in range(key_len):
            key_bits[i] <<= 1
            key_bits[i] |= key[i][j]

    lock_len = len(lock)
    board = [0] * lock_len * 3
    board_len = len(board)
    # 비트마스크 board 리스트
    for i in range(lock_len):
        for j in range(lock_len):
            board[i+lock_len] <<= 1
            board[i+lock_len] |= lock[i][j]
        board[i+lock_len] <<= lock_len

    # 4번 회전해서 확인
    for _ in range(4):
        for row in range(1, lock_len*2):
            for col in range(1, lock_len*2):
                # 열쇠 넣어보기
                attach(row, col, key_len, key_bits, board)
                # lock 가능 check
                if(isFull(lock_len, board)):
                    return True
                # 열쇠 빼기
                detach(row, col, key_len, key_bits, board)
        # 열쇠 돌리기
        key_bits = rotate(key_len, key_bits)

    return False