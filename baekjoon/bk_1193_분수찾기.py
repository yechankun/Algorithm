x = int(input()) 

n = 0
while x > 0:
    n += 1
    x -= n
    

if n%2:
    print("%d/%d"%(1-x, x + n))
else:
    print("%d/%d"%(x + n, 1-x))
 



