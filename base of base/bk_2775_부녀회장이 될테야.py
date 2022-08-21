for _ in range(int(input())):
    k = int(input())
    n = int(input())
    N_list = [x for x in range(1, n+1)]
    for _ in range(k):
        for x in range(1,n):
            N_list[x]+=N_list[x-1]
    print(N_list[n-1])
