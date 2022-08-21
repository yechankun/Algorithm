n = int(input())

str_list = [input() for _ in range(n)]

answer = 0
for st in str_list:
    char_set = set([st[0]])
    for i in range(1,len(st)):
        if not st[i] == st[i-1]:
            if not st[i] in char_set:
                char_set.add(st[i])
            else:
                break
    else:
        answer += 1
print(answer)
