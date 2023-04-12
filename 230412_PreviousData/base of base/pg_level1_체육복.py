def solution(n, lost, reserve):
    answer = 0
    dict_reserve = dict.fromkeys(reserve, 0)
    for l in lost:
        if l in dict_reserve:
            del dict_reserve[l]
            continue
        if l+1 in dict_reserve:
            dict_reserve[l+1]+=1
        if l-1 in dict_reserve:
            dict_reserve[l-1]+=1
    result = [0 for v in dict_reserve.values() if v > 0]
    last = len(lost)-len(result)
    last = last if last > 0 else 0
    
    return n-last


print(solution(5,[2,4],[1,3,5]))
