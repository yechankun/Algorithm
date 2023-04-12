# https://school.programmers.co.kr/learn/courses/30/lessons/12900
def solution(n):
    a= 1
    b= 1
    for i in range(0, n-1):
        fib = (a+b)%1000000007
        a = b
        b= fib
    return b


# 조금 더 가독성 좋게 풀기
'''
def solution(n):
    a,b = 1,2
    for _ in range(2, n):
        a, b = b, (a+b)%1000000007
    return b
'''