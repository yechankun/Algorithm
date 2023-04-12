def solution(bridge_length, weight, truck_weights):
    answer = 0
    i = 0
    curr_weight=0
    curr_on_truck=[0]*bridge_length
    while len(curr_on_truck) and i < len(truck_weights):
        in_truck = truck_weights[i]
        curr_weight -= curr_on_truck.pop(0)
        if curr_weight+in_truck <= weight:
            i+=1
            curr_weight+=in_truck
            curr_on_truck.append(in_truck)
        else:
            curr_on_truck.append(0)
        answer+=1
    return answer+len(curr_on_truck)

print(solution(2,10,[7,4,5,6]))
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(solution(100,100,[10]))
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(solution(5,5,[2, 2, 2, 2, 1, 1, 1, 1, 1]))


