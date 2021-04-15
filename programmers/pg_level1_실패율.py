from collections import Counter
def solution(N, stages):
    stages_counter = Counter(stages)
    visit_nums = [0]*N
    not_clear_nums = [0]*N
    #반복을 최소화, 마지막 스테이지부터 1스테이지까지 순회
    for stage in range(N, 0, -1):
        #반복 첫 시작시
        if stage==N:
            #if 올클이 있는 경우
            if stage+1 in stages_counter:
                visit_nums[stage-1] += stages_counter[stage]+stages_counter[stage+1]  
            else: visit_nums[stage-1] += stages_counter[stage]
            not_clear_nums[stage-1] += stages_counter[stage]
        #그 외
        else:
            visit_nums[stage-1] = stages_counter[stage] + visit_nums[stage]
            not_clear_nums[stage-1] = stages_counter[stage]

    #두 배열을 나누고 스테이지를 가진 zip으로 만듬, 분모가 0인경우엔 0
    result = zip(range(1,N+1), map(lambda x: x[0]/x[1] if x[1] else 0, zip(not_clear_nums, visit_nums)))
    #값을 기반으로 정렬 후 스테이지만 분리
    answer = map(lambda x: x[0] ,sorted(result, key=lambda x: x[1], reverse=True))
    return list(answer)
