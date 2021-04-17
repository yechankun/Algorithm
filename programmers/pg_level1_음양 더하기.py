def solution(absolutes, signs):
    signs = [1 if sign else -1 for sign in signs]
    answer = sum(map(lambda x: x[0]*x[1],zip(absolutes, signs)))
    return answer