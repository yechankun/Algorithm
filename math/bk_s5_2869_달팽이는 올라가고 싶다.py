A,B,V = map(int,input().split())

d, m = divmod(V-B,A-B)

print(d+1 if m else d)
