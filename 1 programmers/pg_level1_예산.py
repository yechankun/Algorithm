def solution(d, budget):
    d.sort()
    answer = 0
    for one in d:
        budget -= one
        if budget < 0:
            break
        answer += 1            
    return answer
