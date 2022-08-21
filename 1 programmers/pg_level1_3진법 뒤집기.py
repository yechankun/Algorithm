def solution(n):
    answer = 0
    result = ""
    r=0
    while n > 2:
        n, r = divmod(n,3)
        result = str(r) + result
    result = str(n) + result
    
    for i, ch_num in enumerate(str(int(result[::-1]))):
        answer += int(ch_num) * 3**i
    
    return answer

print(solution(45))
