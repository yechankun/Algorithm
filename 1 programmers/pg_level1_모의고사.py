def solution(answers):
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]

    count = [0, 0, 0]
    for idx, a in enumerate(answers):
        if a==one[idx%5]: count[0]+=1
        if a==two[idx%8]: count[1]+=1
        if a==third[idx%10]: count[2]+=1  

    return [idx+1 for idx, c in enumerate(count) if c==max(count) and c!=0]