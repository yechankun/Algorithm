# https://school.programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    people.sort()
    boat, i, j = 0, 0, len(people)-1
    while not i>=j:
        if people[i]+people[j] <= limit:
            i+=1
            j-=1
        else:
            j-=1
        boat+=1
    return boat+1 if i==j else boat
