#정규화식 안쓰고 풀기
def solution(new_id):
    answer = ''
    new_id=new_id.lower()
    flag = 1
    for idx, s in enumerate(new_id):
        if s == '.' and flag:
            answer+=s
            flag = 0
        if 'a'<=s<='z' or '0'<=s<='9' or s=='-' or s=='_':
            answer+=s
            flag = 1
    fc, lc = -1, -1
    for idx, s in enumerate(answer):
        if fc==-1 and s != '.':
            fc=idx
            break
    for idx, s in enumerate(answer[::-1]):
        if lc==-1 and s != '.':
            lc=len(answer)-idx
            break
    answer = answer[fc:lc]
    if not answer: answer='a'    

    answer = answer[:15]
    lc = -1
    for idx, s in enumerate(answer[::-1]):
        if lc==-1 and s != '.':
            lc=len(answer)-idx
            break
    answer = answer[:lc]
    
    if len(answer)<3:
        answer += answer[-1]*(3-len(answer))
    
    return answer