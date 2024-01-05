import re

def solution(user_id, banned_id):
    answer = 0
    
    n_banned_id = [s.replace('*', '.') for s in banned_id]
    re_list = [re.compile(user) for user in n_banned_id]
    answer_set = set()
    
    # DFS로 풀 수 있어보임
    def dfs(current, visited, candi):
        if current == len(banned_id):
            answer_set.add(tuple(sorted(list(candi)))) 
            return
        for idx, user in enumerate(user_id):
            if not visited[idx] and len(user)== len(banned_id[current]) and re_list[current].match(user):
                visited[idx] = True
                dfs(current+1, visited, [*candi, idx])
                visited[idx] = False
    dfs(0, [0]*len(user_id), [])
    
    return len(answer_set)