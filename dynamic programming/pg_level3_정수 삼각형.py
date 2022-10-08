# https://school.programmers.co.kr/learn/courses/30/lessons/43105
# 예상 알고리즘: DP
# 베스트 알고리즘: DP

# 첫번째 풀이: 리스트 복사 활용
def solution(triangle):
    sumPath = [0] * len(triangle[-1])
    sumPath[0] = triangle[0][0]
    for i in range(len(triangle)-1):
        tempPath = list(sumPath)
        for j in range(i+1):
            sumPath[j] = max(tempPath[j] + triangle[i+1][j], sumPath[j])
            sumPath[j+1] = max(tempPath[j] + triangle[i+1][j+1], sumPath[j+1])
    return max(sumPath)

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))

# 두번째 풀이: 

def solution(triangle):
    for i in range(1 , len(triangle)):
        for j in range(i+1):
            if j == 0:
                triangle[i][j] += triangle[i-1][0]
            elif j == i:
                triangle[i][j] += triangle[i-1][-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    return max(triangle[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))