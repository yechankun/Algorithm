def solution(a, b):
    a, b = (a, b) if a < b else (b, a)
    return a if a==b else (a+b)*(b-a+1)/2
