def solution(n):
    set_n = set()
    for i in range(1, int(n**0.5)+1):
        if not n%i:
            set_n.add(i)
            set_n.add(n//i)
    return sum(set_n)