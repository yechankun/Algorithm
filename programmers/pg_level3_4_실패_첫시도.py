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

