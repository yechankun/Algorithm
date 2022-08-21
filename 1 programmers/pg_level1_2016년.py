def solution(a, b):
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    dow = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    return dow[(sum(month[:a-1])+b+4)%7]
