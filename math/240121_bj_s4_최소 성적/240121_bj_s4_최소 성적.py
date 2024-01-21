# import
import sys
sys.stdin = open('240121_bj_s4_최소 성적/1.in', 'r')
input = sys.stdin.readline

# A+이 4.5
str_to_score = {'A+': 450, 'A0': 400, 'B+': 350, 'B0': 300, 'C+': 250, 'C0': 200, 'D+': 150, 'D0': 100, 'F': 0}

# solution
def solution(N, X, scores, last):
    # 다음 과목이 추가되었을 때 평균 평점을 계산하는 방법
    # 평균평점에서 과목의 개수를 곱하고, 새로운 과목의 점수를 더한 후, 과목의 개수를 1 더해서 나눈다.

    # 1. 평균 평점을 계산하는 함수
    total = 0
    div = 0
    for i in range(N-1):
        total += scores[i][0] * scores[i][1]
        div += scores[i][0]
    # 원하는 값 계산
    answer = "impossible"
    for i, score in str_to_score.items():
        if X < ((total+last*score)//(div+last))/100:
            answer = i
    return answer

# input
N, X = input().strip().split()
N, X = int(N), float(X)

def convert(x : str):
    if x.isnumeric():
        return int(x)
    else:
        return str_to_score[x]

scores = [list(map(convert, input().strip().split())) for _ in range(N-1)]
last = int(input())

# output
print(solution(N, X, scores, last))