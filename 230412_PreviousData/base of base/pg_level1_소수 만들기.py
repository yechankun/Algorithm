from itertools import combinations
def solution(nums):
    answer = 0
    sum_list = [sum(x) for x in combinations(nums, 3)]
    for sum_num in sum_list:
        for i in range(2, int(sum_num**(1/2))+1):
            if not sum_num % i:
                break
        else:
            answer += 1
    return answer