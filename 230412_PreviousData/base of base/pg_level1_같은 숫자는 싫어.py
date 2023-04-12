def solution(arr):
    tmp=-1
    answer = []
    for i in arr:
        if i==tmp:
            continue
        else:
            tmp=i
            answer.append(i)        
    return answer