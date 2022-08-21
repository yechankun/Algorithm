import itertools
def solution(clothes):
    dict_clothes = {}
    for cloth in clothes:
        if cloth[1] in dict_clothes:
            dict_clothes[cloth[1]] += [cloth[0]]
        else:
            dict_clothes[cloth[1]] = [cloth[0]]
    list_kind=[0]*len(dict_clothes)
    for idx, cloth in enumerate(dict_clothes):
        list_kind[idx] = list(itertools.permutations(cloth))
    print(list_kind)
    return 0


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
