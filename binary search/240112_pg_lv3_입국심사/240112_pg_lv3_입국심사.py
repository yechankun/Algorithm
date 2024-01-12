# 이분탐색 문제인듯
def solution(n, times):    
    left, right = 0, max(times) * n
    
    while left <= right:
        middle = (left + right)//2
        
        count = 0
        for time in times:
            count += middle//time
        if count < n:
            left = middle + 1
        else:
            right = middle - 1
    return left