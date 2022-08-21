def isCorrect(w):
    cnt=0
    for c in w:
        if c=='(': cnt+=1
        else:
            cnt-=1
            if cnt==-1: return False        
    return cnt==0

def solution(p):
    return isCorrect(p)