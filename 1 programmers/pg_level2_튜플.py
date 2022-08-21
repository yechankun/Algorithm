from collections import Counter
def solution(s):
    a = s.replace('{', '').replace('}', '').replace(',', ' ').split()   
    return list(map(lambda x: int(x[0]), Counter(a).most_common()))

