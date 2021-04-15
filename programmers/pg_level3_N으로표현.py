def solution(N, number):
    if(number==N):return 1
    result = [set() for x in range(8)]
    result[0].add(N)

    for i in range(1, 8):
        for j in range(0, i):
            k=i-j-1
            for a in result[j]:
                for b in result[k]:
                    result[i].add(a+b)
                    result[i].add(a*b)
                    if a-b > 0:result[i].add(a-b)
                    if int(a/b) > 0:result[i].add(int(a/b))
        result[i].add(int(str(N)*(i+1)))
        if(number in result[i]):
            return i+1
    return -1

print(solution(5,5))
