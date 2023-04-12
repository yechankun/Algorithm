# https://school.programmers.co.kr/learn/courses/30/lessons/42578?language=python3
from collections import Counter
from functools import reduce
def solution(clothes):
    cnt = Counter(map(lambda x:x[1], clothes))
    return reduce(lambda x, y: x*y, map(lambda x:x+1,cnt.values()))-1