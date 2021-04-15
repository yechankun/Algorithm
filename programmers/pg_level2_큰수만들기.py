'''
def solution(number, k):
    last = 0
    answer = ""
    i = 1
    #number의 크기에서 k를 빼서 첫번째 숫자의 자리수를 구한다. len(number)=5고 k=2일 때 자리수는 
    #리턴의 자리수는 len(number) - k = 3 => 100의자리다.
    #number에서 부분 문자열를 떼네서 계산한다. 위 예시에서라면 정답이 100의 자리이므로 number[:5-2]이다.
    #따라서 number[:len(number)-(len(number)-k)+1]=number[:k+1]이 된다.
    #이를 모든 자리에서 반복해야하므로 (100=>10=>1) 이를 조절하기 위해 i를 사용한다.
    while k+i<=len(number):
        m = last, number[last]
        for idx, c in enumerate(number[last+1:k+i]):
            if m[1] < c:
                m = last+1+idx, c
        last = m[0]+1; answer += m[1]; i += 1;
        print(answer, 'answer')
        print(last, 'last')
        print(number[last+1:k+i], 'next number')
    
    return answer
'''

'''
def solution(number, k):
    last, i = 0, 1
    answer = ""
    while k+i<=len(number):
        m_idx, m = last, number[last]
        for idx in range(last+1, k+i):
            if m[1] < number[idx]:
                m = idx, number[idx]
                if number[idx] == 9:
                    break;
        last = m_idx+1; 
        answer += m; i += 1;
    return answer

print(solution("4177252841", 4))
'''

def solution(number, k):
    alist = [number[0]]
    for num in number[1:]:
        while len(alist) > 0 and alist[-1] < num and k > 0: 
        #바꾸는 경우- 새로들어온수가 기존수보다 크거나, k가 0이 안됐거나, alist 0개가 아닐때 
            k -= 1
            alist.pop()
        alist.append(num) #항상 append
    if k != 0: #for문 다 돌았는데 k가 안찼을때 
        alist = alist[:-k]
    return ''.join(alist)

print(solution("4177252841", 4))
