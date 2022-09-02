def solution(lottos, win_nums):
    R = set(lottos) & set(win_nums)
    win = {6:1, 5:2, 4:3, 3:4, 2:5}
    answer = [win.get(len(R)+lottos.count(0), 6), win.get(len(R), 6)]
    return answer