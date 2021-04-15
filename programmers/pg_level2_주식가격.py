def solution(prices):
    prs_len = len(prices)
    stk_list=[0]*prs_len
    idx_list=[[] for _ in range(prs_len)]
    answer=[0]*prs_len
    top=-1

    for idx, p in enumerate(prices):
        if top != -1:
            if stk_list[top] == p:
                idx_list[top]+=[idx]
            elif stk_list[top] > p:
                for i in idx_list[top]:
                    answer[i] = idx-i
                idx_list[top] = []
                top-=1
                for s in stk_list[top-prs_len::-1]:
                    if s >  p:
                        for i in idx_list[top]:
                            answer[i] = idx-i
                        idx_list[top] = []
                        top-=1
                    elif s == p: idx_list[top]+=[idx]
                    else: break
            top+=1
            stk_list[top]=p
            idx_list[top]+=[idx]
        else:
            top=0
            stk_list[top]=p
            idx_list[top]+=[idx]
    for idx in idx_list[:top+1]:
        for i in idx:
            answer[i] = prs_len-i-1

    return answer


#더 나은 풀이
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer
