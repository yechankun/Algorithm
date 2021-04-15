target = int(input())
m = int(input())
arr = set(input().split()) if m else []
mindiff = abs(target - 100)
for i in range(1000001):
    numstr = str(i)
    for c in numstr:
        if c in arr:
            break
    else:
        mindiff = min(mindiff, abs(target - i) + len(str(i)))     
print(mindiff)
