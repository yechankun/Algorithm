# https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = len(s)
    for i in range(1,len(s)//2+1):
        out = [s[k:k+i] for k in range(0, len(s), i)]
        tmp = out[0]
        count = 1
        ck = ""
        for o in out[1:]:
            if tmp == o:
                count+=1
            else:
                ck+=("" if count==1 else str(count))+tmp
                tmp=o
                count=1
        else:
            if tmp == o:
                ck+=("" if count==1 else str(count))+tmp
        if len(ck) < answer:
            answer = len(ck)
    return answer
