import datetime
import re
def date_int_map(date_s, float_s):
    return [datetime.datetime.strptime(date_s, "%Y-%m-%d %H:%M:%S.%f"), float(float_s)]

def solution(lines):
    answer = 0
    n=0
    tmp_list = [date_int_map(*re.findall("\S+ \S+|[^ ^s]+", l)) for l in lines] 
    
    for idx, (d, s) in enumerate(tmp_list):
        for d2, s2 in tmp_list[idx:]:
            delta = (d2-d).total_seconds()
            if round(delta-s2+0.001,3) < 1.0:
                n+=1
        answer = max(answer, n)
        n=0
    return answer