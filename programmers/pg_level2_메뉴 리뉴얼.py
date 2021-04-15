from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for course_size in course:
        com = []
        for order in orders:
            com += combinations(sorted(order), course_size)
        candi = Counter(com).most_common()
        answer += [menu for menu, cnt in candi if cnt > 1 and cnt == candi[0][1]]
    return [''.join(v) for v in sorted(answer)]
