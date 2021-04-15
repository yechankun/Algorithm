def solution(citations):
    citations.sort(reverse=True)
    m = 0
    for i in range(len(citations)):
        if m < min(citations[i],i+1):
            m = min(citations[i],i+1)
    return m
