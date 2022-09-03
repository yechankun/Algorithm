# https://school.programmers.co.kr/learn/courses/30/lessons/77486
import math
def solution(enroll, referral, seller, amount):
    referral_set = set(referral)

    answer = [0] * len(enroll)

    stack = [enroll[0]]
    people_dict = {people:idx for idx, people in enumerate(enroll)}

    for idx, people in enumerate(seller):
        answer[people_dict[people]] += math.ceil(amount[idx]*90)
        curr_people = people
        curr_tax = math.floor(amount[idx]*10)
        while not referral[people_dict[curr_people]] == '-':
            answer[people_dict[referral[people_dict[curr_people]]]] += math.ceil(curr_tax*0.9)
            curr_tax = math.floor(curr_tax*0.1)
            curr_people = referral[people_dict[curr_people]]
    return answer


# 시간 복잡도 더 좋은 풀이2
'''
def solution(enroll, referral, seller, amount):
    money = [0 for _ in range(len(enroll))]
    dict = {}
    for i, e in enumerate(enroll):
        dict[e] = i
    for s, a in zip(seller, amount):
        m = a * 100
        while s != "-" and m > 0:
            idx = dict[s]
            money[idx] += m - m//10
            m //= 10
            s = referral[idx]
    return money
'''

# 시간 복잡도가 더 좋은 풀이
'''
def find(parents, money, number, answer):
    # 민호까지 돈이 들어오거나 줄 돈이 없으면 종료
    if parents[number] == number or money // 10 == 0:
        answer[number] += money
        return
    send = money // 10
    mine = money - send
    answer[number] += mine
    find(parents, send, parents[number], answer)
    return


def solution(enroll, referral, seller, amount):
    n = len(enroll)  # 총 사람 수(민호 포함 X)
    answer = [0] * (n + 1)  # 민호 포함
    d = {}  # 이름-번호의 key-value를 가지는 딕셔너리
    parents = [i for i in range(n + 1)]  # 각자 자신을 부모로 초기화
    # 이름-번호로 딕셔너리에 저장
    for i in range(n):
        d[enroll[i]] = i + 1
    # 추천인 입력
    for i in range(n):
        if referral[i] == "-":  # 민호가 추천인
            parents[i + 1] = 0
        else:
            parents[i + 1] = d[referral[i]]
    # 칫솔 정산
    for i in range(len(seller)):
        find(parents, amount[i] * 100, d[seller[i]], answer)
    return answer[1:]
'''