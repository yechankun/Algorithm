# https://school.programmers.co.kr/learn/courses/30/lessons/42746
#내 풀이
def solution(numbers):
    numbers = list(map(str,numbers))
    st = [0, len(numbers)-1]    
    l, r=0, 0
    while st:
        r = st.pop(-1)
        l = st.pop(-1)
        p = numbers[r]
        i = l        
        for j in range(l, r):
            if p+numbers[j] < numbers[j]+p:
                numbers[j], numbers[i] = numbers[i], numbers[j]
                i+=1
        numbers[r], numbers[i] = numbers[i], p
        if i - 1 > l:
            st.extend([l, i - 1])
        if i + 1 < r:
            st.extend([i + 1, r])
    return str(int(''.join(numbers)))
print(solution(['9', '66', '6', '60', '22', '2', '10']))

'''#베스트풀이
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
'''

a=[]
for i in range(10000):
    a.append(i)

import time


start = time.time()

a = [str(i) for i in a]

two_start = time.time()

a = list(map(str, a))

end = time.time()
print("1 시간=", two_start-start)
print("2 시간=", end-two_start)
