def solution(a):
    if len(a)<3:
        return len(a)
    answer = 0
    left_min = []
    right_min = []
    
    n_min = 1000000001
    for i in a:
        if n_min>i:
            n_min = i
        left_min.append(n_min)
    n_min = 1000000001
    for i in a[::-1]:
        if n_min>i:
            n_min = i
        right_min.append(n_min)
    right_min.reverse()

    answer+=2
    for i in range(1, len(a)-1):
        if a[i]<max(left_min[i-1],right_min[i+1]):
            answer+=1
    return answer


print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))
