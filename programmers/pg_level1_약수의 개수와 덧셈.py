#내 풀이
def solution(left, right):
    answer = 0
    for n in range(left, right+1):
        cnt = 0
        for i in range(1, int(n**0.5) + 1): 
            if (n % i == 0):            
                cnt += 1
                if (i != (n // i)): 
                    cnt += 1
        answer += -n if cnt%2 else n
    return answer

#더 나은 풀이. 약수의 개수가 짝수, 홀수가 나올 조건을 판단함.
def solution1(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer