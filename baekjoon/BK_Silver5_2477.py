K = int(input())
bean = []
maxW, maxH = 0, 0
for i in range(6):
    bean.append(int(input().split()[1]))
    if(i%2 ==0):
        maxW = max(bean[i], maxW)
    else:
        maxH = max(bean[i], maxH)
big = maxW * maxH
smallW, smallH = 0, 0
for i in range(6):
    if i % 2 == 0 :
        if bean[(i + 5) % 6] + bean[(i + 1) % 6] == maxH:
            smallW = bean[i]
    else:
        if bean[(i + 5) % 6] + bean[(i + 1) % 6] == maxW:
            smallH = bean[i]
diff = smallW * smallH
print(K * (big - diff))
