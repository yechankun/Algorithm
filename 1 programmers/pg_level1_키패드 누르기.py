def solution(numbers, hand):
    answer = ''
    keypad = [[1,4,7],[2,5,8,0],[3,6,9]]
    #현재위치 left손, right손
    left_hand, right_hand = [0, 3], [2, 3]
    hand_dict = {"right":"R", "left":"L"}
    for num in numbers:
        for x_idx, key_row in enumerate(keypad):
            for y_idx, key in enumerate(key_row):
                if key==num:
                    if x_idx == 0:
                        answer+='L'
                        left_hand[0], left_hand[1] = x_idx, y_idx
                        break
                    elif x_idx == 2:
                        answer+='R'
                        right_hand[0], right_hand[1] = x_idx, y_idx
                        break
                    else:
                        left_dist = (lambda x,y:[abs(x[0]-y[0]),abs(x[1]-y[1])])(left_hand, (x_idx, y_idx))
                        right_dist = (lambda x,y:[abs(x[0]-y[0]),abs(x[1]-y[1])])(right_hand, (x_idx, y_idx))
                        dist_result = sum(left_dist) - sum(right_dist)
                        if dist_result < 0:
                            answer+='L'
                            left_hand[0], left_hand[1] = x_idx, y_idx
                            break
                        elif dist_result > 0:
                            answer+='R'
                            right_hand[0], right_hand[1] = x_idx, y_idx
                            break         
                        else:
                            if hand == "left":
                                answer+='L'
                                left_hand[0], left_hand[1] = x_idx, y_idx
                            else:
                                answer+='R'
                                right_hand[0], right_hand[1] = x_idx, y_idx
                            break
            else: continue
            break            
    return answer
