# https://school.programmers.co.kr/learn/courses/30/lessons/68645
def solution(n):
    arr = [[0] * _ for _ in range(1,n+1)]  
    x, y, num = 0, -1, 1
    for i in range(n):
        for j in range(i, n):
            if not i % 3:
                y+=1
            elif i % 3 == 1:
                x+=1
            else:
                y-=1; x-=1
            arr[y][x] = num
            num+=1
    return sum(arr, [])

