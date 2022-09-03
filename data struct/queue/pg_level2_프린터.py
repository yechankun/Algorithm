# https://school.programmers.co.kr/learn/courses/30/lessons/42587
def solution(priorities, location):
    i=0
    prior_idxs = [idx for idx in range(len(priorities))]
    # print(prior_idxs)
    while i<len(priorities)-1:
        if priorities[i]<max(priorities[i+1:]):
            priorities.append(priorities.pop(i))
            prior_idxs.append(prior_idxs.pop(i))
            i-=1
        i+=1
    # print(prior_idxs)
    return prior_idxs.index(location)+1

# print(solution([1, 1, 9, 1, 1, 1], 0))

# 다른 좋은 풀이
'''
def solution(p, l):
    ans = 0
    m = max(p)
    while True:
        v = p.pop(0)
        if m == v:
            ans += 1
            if l == 0:
                break
            else:
                l -= 1
            m = max(p)
        else:
            p.append(v)
            if l == 0:
                l = len(p)-1
            else:
                l -= 1
    return ans
'''