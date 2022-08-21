def solution(n):
    search_list = [1 for i in range(n+1)] #0, 1은 사용하지 않음
    for idx in range(2, n+1):
        for i in range(2, int(idx**0.5)+1):
            if not (idx)%i:
                search_list[idx] = 0
                break
        else:
            continue
        for i in range(idx*idx, n+1, idx):
            search_list[i] = 0
    return search_list.count(1) - 2


#가장 나은 방식
def solution2(n):
    num = set(range(3, n+1, 2))

    for i in range(3, int(n**0.5)+1):
        if i in num:
            num-=set(range(i*i,n+1,i))
    return len(num)+1
