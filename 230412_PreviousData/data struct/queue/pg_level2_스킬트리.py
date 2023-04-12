# https://school.programmers.co.kr/learn/courses/30/lessons/49993?language=python3
def solution(skill, skill_trees):
    answer = 0
    for st in skill_trees:
        last_idx = 0
        is_fail = False
        for st_sk in st:
            for s_idx, s in enumerate(skill[last_idx:]):
                if s==st_sk:
                    if s_idx+last_idx != last_idx:
                        is_fail = True
                        break;
                    last_idx += 1
                    break;
            if is_fail: break;
        if not is_fail: answer += 1
        else: is_fail = False
    return answer

# 내 풀이는 큐가 아니지만 베스트 케이스는 큐로 푸는 방식임

# 다른 사람이 큐로 푼 방식
'''
def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer
'''