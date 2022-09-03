# https://school.programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    for i in range(1, int(yellow**0.5)+1):
        if not yellow%i:
            b_x = yellow//i+2
            if b_x*2+i*2==brown:
                return [b_x, i+2]
