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

