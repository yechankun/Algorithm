def solution(N, number):
    if(N==number): return 1
    list = [set() for x in range(9)]
    list[1].add(N)
    
    for i in range(2, 9):
        for j in range(1, i):
            k = i-j
            for a in list[j]:
                for b in list[k]:
                    list[i].add(a+b)
                    list[i].add(a-b)
                    list[i].add(a*b)
                    if b != 0: list[i].add(a//b)
        list[i].add(int(str(N)*(i)))
        if number in list[i]:return i
    return -1