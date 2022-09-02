def solution(numbers):
    answer = set()
    for i, i_num in enumerate(numbers):
        for j, j_num in enumerate(numbers):
            if i==j: continue
            answer.add(i_num+j_num)
    answer_list = list(answer)
    answer_list.sort()
    
    return answer_list

print(solution([2,1,3,4,1]))
