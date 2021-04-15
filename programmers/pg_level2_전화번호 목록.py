def solution(phone_book):
    set_list = set(phone_book)
    for number in phone_book:
        tmp = ''
        for c in number[:-1]:
            tmp += c
            if tmp in set_list: return False;
    return True
