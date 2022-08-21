import sys
T = int(input())

for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    d, m = divmod(N, H)
    if m: d, m = m,1+d
    else: d, m = H,d
    print("%d%02d"%(d, m))
