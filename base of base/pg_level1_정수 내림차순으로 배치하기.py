def solution(n):
    str_n = list(str(n))
    str_n.sort(reverse=True)
    return int(''.join(str_n))