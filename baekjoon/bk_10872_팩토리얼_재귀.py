N = int(input())

N_list = [1, 1] + [0] * 11

def fact(N):
    if N_list[N]:
        return N_list[N]
    N_list[N] = N * fact(N-1)
    return N_list[N]
        
print(fact(N))
