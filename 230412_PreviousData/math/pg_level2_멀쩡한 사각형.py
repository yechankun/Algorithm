# https://school.programmers.co.kr/learn/courses/30/lessons/62048
import math
def solution(w,h):
    i, sum=1, 0
    while h*i/w-math.floor(h*i/w) != 0:
        sum += math.ceil(h*i/w)-math.floor(h*(i-1)/w)
        i+=1
    sum += math.ceil(h*i/w)-math.floor(h*(i-1)/w)
    return w*h-sum*w/i

print(solution(100000000,100000000))

'''
import math
import decimal
def solution(w,h):
    if(h<w):
        w, h= h, w
    if w == 1 or h == 1: return 0
    grad = decimal.Decimal(h)/decimal.Decimal(w)
    i, sum=1, 0
    while grad*i-math.floor(grad*i) != 0:
        sum += math.ceil(grad*i)-math.floor(grad*(i-1))
        i+=1
    sum += math.ceil(grad*i)-math.floor(grad*(i-1))
    return int(w*h-sum*h//(grad*i))

import math
def solution(w,h):
    if(h<w):
        w, h= h, w
    if w == 1 or h == 1: return 0
    i, sum=1, 0
    while h*i/w-math.floor(h*i/w) != 0:
        sum += math.ceil(h*i/w)-math.floor(h*(i-1)/w)
        i+=1
    sum += math.ceil(h*i/w)-math.floor(h*(i-1)/w)
    return w*h-sum*h/(h*i/w)'''
