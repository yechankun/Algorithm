# https://school.programmers.co.kr/learn/courses/30/lessons/12921
import itertools, math
def solution(numbers):    
    num_set={int("".join(n)) for n in 
              [n for i in range(1, len(numbers)+1) for n in itertools.permutations(numbers, i)]}

    num_set={n for n in num_set if (n%2==1 or n==2) and not n == 1}

    print(num_set)
    answer=0
    for n in num_set:
        for i in range(3, math.ceil(math.sqrt(n))+1):
            if not n%i:
                break;
        else:
            print(n)
            answer+=1
    return answer
