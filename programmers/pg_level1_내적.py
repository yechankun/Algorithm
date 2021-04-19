def solution(a, b):
    answer = sum(map(lambda x: x[0]*x[1], zip(a, b)))
    return answer