# https://school.programmers.co.kr/learn/courses/30/lessons/17686
# 풀이 알고리즘: 정렬

# 사용자 지정 정렬 옵션을 만들어서 정렬한다.
def customsort(x):
    idx_l, idx_r = 0, len(x)
    for idx, v in enumerate(x):
        if v.isnumeric() and idx_l == 0:
            idx_l = idx
        elif idx_l != 0 and not v.isnumeric() and idx_r == len(x):
            idx_r = idx
    return (x[:idx_l].upper(), int(x[idx_l:idx_r]))


def solution(files):
    # 문자열을 순회하면서 첫 글자가 숫자인 것까지를 계속 탐색하면 된다.
    files.sort(key=customsort)
    return files
