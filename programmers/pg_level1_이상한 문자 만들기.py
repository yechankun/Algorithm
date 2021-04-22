def solution(s):
    splited_s = s.split(" ")
    trans_s = ["".join([small_s[i].lower() if i%2 else small_s[i].upper() 
                        for i in range(len(small_s))]) for small_s in splited_s]
    answer = ' '.join(trans_s)
    return answer