# https://school.programmers.co.kr/learn/courses/30/lessons/12909?language=python3
# 스택을 대체하는 덧셈 뺄셈을 이용한 풀이
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


# 다른 사람의 풀이
# 베스트케이스가 아니지만 문제의 의도는 스택임

'''
def solution(s):
    stack = []
    for i in s:
        if i == '(':  # '('는 stack에 추가
            stack.append(i)
        else:  # i == ')'인 경우
            if stack == []:  # 괄호 짝이 ')'로 시작하면 False 반환
                return False
            else:
                stack.pop()  # '('가 ')'와 짝을 이루면 stack에서 '(' 하나 제거
    
    return stack==[]
'''