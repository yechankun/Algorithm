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