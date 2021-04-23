s=input()+' ' 
lf=0;rf=0;c=0
for k in s:
    if k == ' ':
        if rf:
            c+=1
        rf=0
    else:
        rf=1
print(c)

