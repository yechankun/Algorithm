# https://school.programmers.co.kr/learn/courses/30/lessons/72412
from itertools import combinations as COM
def solution(info, query):
    answer=[]
    dict_hashmap = {}
    for ifs in info:
        i = ifs.split()
        kinds = i[:-1]
        score = int(i[-1])
        for n in range(5):
            for h in [' '.join(c) for c in (COM(kinds,n))]:
                if h in dict_hashmap:
                    dict_hashmap[h].append(score)
                else:
                    dict_hashmap[h] = [score]
    for d in dict_hashmap.values():
        d.sort()
    for qs in query:   
        q = qs.replace('-', '').replace('and','').split()
        key = ' '.join(q[:-1])
        if key in dict_hashmap:
            score_list = dict_hashmap[key]
            qry_score = int(q[-1])
            left, right = 0, len(score_list)
            while (left < right):
                mid = (left + right)//2
                if score_list[mid] < qry_score:
                    left = mid + 1
                else:
                    right = mid
            answer.append(len(score_list)-right)
        else:
            answer.append(0)
    return answer
