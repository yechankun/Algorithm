# import
import sys
sys.stdin = open('1.in', 'r')
input = sys.stdin.readline

# 풀이
def solution(a, b, c, x, y):
    # 임의의 위치에 공백을 삽입해 문자열의 길이를 같게 한다.

    # 적절히 공백을 추가했을 때 최대 총점을 구해야 한다.

    # 1. 두 문자가 같으면 A(>0)점을 받음
    # 2. 두 문자가 적어도 하나가 공백이면 B(<0)점을 받음
    # 3. 공백이 아니고 서로 다르면 C(<0) 점을 받음

    # 문자열 x y는 최대 3000자
    # 문자열이 최대한 유사하게 만들어야 됨

    # a bc
    #   dc
    # 문자열의 순서만 같으면 점수를 추가할 수 있다   
    # abcdef
    # efabcd

    # 문자열의 비교를 DP와 같은 방식으로 해야한다
    '''
    1 -2 -1
        a   b   c   d   e   f
    e   -1  -3 -5  -7  -6  -8
    a   -1  -2 -4  -6  -8  -8
    b   -3   0 -2  -4  -6  -8  
    f   -5
    '''
    # 위와 같이 비교가 이루어지면 될것이다
    # 이를 위해 2차원 배열을 만들어야 한다
    diff = [[0] * (len(x)+1) for _ in range(len(y)+1)]
    for i in range(1, len(y)+1):
        diff[i][0] = diff[i-1][0] + b
    for j in range(1, len(x)+1):
        diff[0][j] = diff[0][j-1] + b

    for i in range(1, len(y)+1):
        for j in range(1, len(x)+1):
            diff[i][j] = max(diff[i-1][j] + b, diff[i][j-1] + b, diff[i-1][j-1] + (a if x[j-1] == y[i-1] else c))
    
    print(diff[-1][-1])

    return

# 입력
a, b, c = map(int, input().split())

x = input().strip()
y = input().strip()

solution(a, b, c, x, y)