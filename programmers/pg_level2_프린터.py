def solution(priorities, location):
    i=0
    prior_idxs = [idx for idx in range(len(priorities))]
    print(prior_idxs)
    while i<len(priorities)-1:
        if priorities[i]<max(priorities[i+1:]):
            priorities.append(priorities.pop(i))
            prior_idxs.append(prior_idxs.pop(i))
            i-=1
        i+=1
    print(prior_idxs)
    return prior_idxs.index(location)+1

print(solution([1, 1, 9, 1, 1, 1], 0))

