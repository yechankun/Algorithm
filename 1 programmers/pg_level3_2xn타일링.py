def solution(n):
    a= 1
    b= 1
    for i in range(0, n-1):
        fib = (a+b)%1000000007
        a = b
        b= fib
    return b