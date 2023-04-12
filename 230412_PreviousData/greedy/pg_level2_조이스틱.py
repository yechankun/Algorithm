# https://school.programmers.co.kr/learn/courses/30/lessons/42860?language=python3
def solution(name):
    answer = 0
    min_travel, max_tmp, a_idx_tmp = len(name)-1, 0, 0
    answer += 13-abs(ord(name[0])-78)
    for idx, cur in enumerate(name[1:]):
        answer += 13-abs(ord(cur)-78)
        if cur == 'A':
            if not max_tmp: a_idx_tmp = idx
            max_tmp+=1
        else:
            if max_tmp:
                min_travel_tmp = len(name)-max_tmp+a_idx_tmp-1
                if min_travel > min_travel_tmp : min_travel = min_travel_tmp 
            max_tmp=0
            a_idx_tmp=0
    else:
        if max_tmp:
            min_travel_tmp = len(name)-max_tmp-1
            if min_travel > min_travel_tmp : min_travel = min_travel_tmp
    answer += min_travel
    return answer

print(solution("AABAAAAAB"))
