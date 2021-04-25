n = int(input()) - 1

answer = 1
while n > 0:
    n -= answer*6
    answer += 1
else:
    print(answer)

