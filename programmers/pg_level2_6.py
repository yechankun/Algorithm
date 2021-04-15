#최선의 시간복잡도를 생각해봤습니다.다만 try except의 시간복잡도는 잘 모르겠습니다
def solution(prices):
    prs_len = len(prices)
    stk_list=[0]
    answer=[0]*prs_len

    for idx, p in enumerate(prices[1:]):
        if prices[stk_list[-1]] > p:
            for s in stk_list[::-1]:
                if prices[s] > p:
                    answer[s] = idx-s+1
                    stk_list.remove(s)
                else: break
        stk_list.append(idx+1)

    for i in range(0, len(stk_list)-1):
            answer[stk_list[i]] = prs_len-stk_list[i]-1
    
    return answer

"""
a = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(a[-1])

a=[[]]*7
print(a)
a[0]+=[1]
print(a)
print("//////")

a=[[],[],[],[]]*7
a[0]+=[1]
print(a)
print(a[0],"이거다")
print("//////")

a = [[] for _ in range(7)]
print(a)
a[0]+=[1]
print(a)
"""
print (solution([5, 8, 6, 2, 4, 1]))


""" list [1 2 3 2
list [[0],[1,3],[2]]"""
