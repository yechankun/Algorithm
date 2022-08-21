def isCorrect(w):
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
            print(num)
            if not num:
                u=w[:idx+1]
                v=w[idx+1:]
                break;
            
            '''if w[idx+1:].startswith(u.replace(')','.').replace('(',')').replace('.','(')):
                u = w[:(idx+1)*2];v = w[(idx+1)*2:]
                break'''
        print(u, 'u입니다.')
        print(v, 'v입니다.')
        print(isCorrect(u),'u는 맞나?')
        if isCorrect(u):
            return u+recursion(v)
        else:
            e = "("+recursion(v)+")"
            print(e,'e는 뭐지?', u, 'u는 뭐지?')
            #e += u[-2:0:-1]
            e += u[1:-1].replace(')','.').replace('(',')').replace('.','(')
            print(e, "결과 e")
            return e
    else:
        return ""

def solution(p):
    return recursion(p)



def check(w):
    if len(w):
        u = ""
        v = ""
        for idx, s in enumerate(w):
            u += s
            if w[idx+1:].startswith(u.replace(')','.').replace('(',')').replace('.','(')):
                u = w[:(idx+1)*2];v = w[(idx+1)*2:]
                break
        print(u);print(v)


print(solution("((()()(())))()"))

'''
    ck = []
    for s in w:
        if s=='(':
            ck.append(s)
        else:
            for i in range(-1, -1-len(ck),-1):
                print(i)
                if ck[i] == ")":
                    return False
                else:
                    del ck[i]
                    break;
            else: return False
    return False if len(ck) else True
'''


'''
    u=""
    v=""
    for idx, s in enumerate(p):
            u += s
            if p[idx+1:].startswith(u[::-1].replace(')','.').replace('(',')').replace('.','(')):
                u = p[:(idx+1)*2];v = p[(idx+1)*2:]
                break

'''


