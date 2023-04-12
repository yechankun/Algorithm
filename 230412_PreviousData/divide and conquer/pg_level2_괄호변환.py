def is_correct(w):
    cnt=0
    for c in w:
        if c=='(': cnt+=1
        else:
            cnt-=1
            if cnt==-1: return False
    return True

def recursion(w):
    if len(w):
        num=0
        u, v= "",""
        for idx, s in enumerate(w):            
            if s == "(": num+=1
            else: num-=1
            if not num: u=w[:idx+1]; v=w[idx+1:]; break
        if is_correct(u):
            return u+recursion(v)
        else:
            e = "("+recursion(v)+")"
            e += u[1:-1].replace(')','.').replace('(',')').replace('.','(')
            return e
    else:
        return ""

def solution(p):
    return recursion(p)

##다른 풀이
'''
def solution(p):
    if p=='': return p
    r=True; c=0
    for i in range(len(p)):
        if p[i]=='(': c-=1
        else: c+=1
        if c>0: r=False
        if c==0:
            if r:
                return p[:i+1]+solution(p[i+1:])
            else:
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))
'''