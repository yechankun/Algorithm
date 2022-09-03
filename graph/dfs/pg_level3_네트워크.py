# https://school.programmers.co.kr/learn/courses/30/lessons/43162
def solution(n, computers):
    answer = 0
    visited_l = [False for i in range(n)]
    for idx_com in range(n):
        if not visited_l[idx_com]:
            answer += 1
            DFS(n, computers, idx_com, visited_l)
    return answer

def DFS(n, computers, idx_com, visited_l):
    visited_l[idx_com] = True
    for connect_com in range(n):
        if idx_com != connect_com and computers[idx_com][connect_com]:
            if not visited_l[connect_com]:
                DFS(n, computers, connect_com, visited_l)
