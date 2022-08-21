from collections import Counter
c=Counter(input().upper())
m=c.most_common(2)
print('?'if len(m)-1 and m[0][1]==m[1][1]else m[0][0])
