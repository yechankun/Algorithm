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
