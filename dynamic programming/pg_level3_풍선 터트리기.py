# https://school.programmers.co.kr/learn/courses/30/lessons/68646
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

# 다른 사람의 좋은 풀이
'''
def solution(a):
    result = [False for _ in range(a)]
    minFront, minRear = float("inf"), float("inf")
    for i in range(len(a)):
        if a[i] < minFront:
            minFront = a[i]
            result[i] = True
        if a[-1-i] < minRear:
            minRear = a[-1-i]
            result[-1-i] = True
    return sum(result)
'''

# 실패했던 풀이 1
'''
def solution(a):
    answer = 0
    flag=0
    
    for idx, i in enumerate(a):
        try:
            if i>min(a[idx+1:]):
                flag+=1
            if i>min(a[:idx]):
                flag+=1
        except:
            flag=0
            continue
        if flag==2:
            answer+=1
        flag=0

    return len(a)-answer

print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))
'''

# 실패했던 풀이2
'''
def solution(a):
    answer = 0
    sort_idx_d=dict(zip(sorted(a),range(len(a))))
    sort_val_idx=[y for x,y in sorted(zip(a,range(len(a))),key=lambda x:x[0])]

    l_flag=0
    r_flag=0
    
    for idx, i in enumerate(a):
        for j in sort_val_idx[:sort_idx_d[i]]:
            if r_flag and l_flag:
                break
            if j>sort_val_idx[sort_idx_d[i]]:
                r_flag=1
                continue
            if j<sort_val_idx[sort_idx_d[i]]:
                l_flag=1
                continue
        if r_flag and l_flag:
            answer+=1
        l_flag=0
        r_flag=0

    return len(a)-answer

print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))
'''