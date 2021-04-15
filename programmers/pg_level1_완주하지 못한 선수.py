from collections import Counter
def solution(participant, completion):
    p, c = Counter(participant), Counter(completion)
    return list((p-c).elements())[0]
