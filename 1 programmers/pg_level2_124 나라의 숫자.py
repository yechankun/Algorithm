def solution(n): 
    j=(n-1)//3
    k = n%3
    if not k:k = 4
    if not j: return str(k)
    answer = str(k)
    while j>0:
        k=j%3
        if not k:k = 4
        answer = str(k)+answer
        j=(j-1)//3
    return answer


#조금 더 나은 풀이
def solution2(n): 
    num = ['1','2','4']
    answer = ""


    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer
