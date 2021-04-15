'''
import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while len(scoville) > 1:
        ls = heapq.heappop(scoville)
        ls_s = heapq.heappop(scoville)
        if ls < K:
            ls_s = ls + ls_s*2
            answer += 1
            heapq.heappush(scoville, ls_s)
        else: break;
    return answer if scoville[0] > K else -1
'''

'''
def solution(scoville, K):
    answer = 0
    scoville.sort()
    top = 0
    length = len(scoville) - 1
    while top < length:
        if scoville[top] < K:
            scoville[top+1] = scoville[top] + scoville[top+1]*2
            answer += 1
            top += 1
            scoville.sort()
        else: break;
    return answer if scoville[top] > K else -1
'''

import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer

print(solution([1,2,3,9,10,12], 7))
print(solution([1,2], 7))

