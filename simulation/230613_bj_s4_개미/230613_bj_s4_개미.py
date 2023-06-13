import sys
input = sys.stdin.readline

def solution():
    N1, N2 = map(int, input().split())
    ants1 = list(reversed(input().rstrip())) 
    ants2 = list(input().rstrip())
    time = int(input())

    answer = ants1 + ants2
    NS1, NS2 = set(ants1), set(ants2)
    for _ in range(time):
        for i in range(len(answer)-1):
            if answer[i] in NS1 and answer[i+1] in NS2:
                answer[i], answer[i+1] = answer[i+1], answer[i]
                if answer[i+1] == ants1[-1]:
                    break
    print(''.join(answer))

solution()

# # 테스트
# for i in range(1, 5):
#     sys.stdin = open('simulation/230609_bj_s4_개미/%d.in' % i, 'r')
#     input = sys.stdin.readline
#     print(i, '풀이: ', end='')
#     solution()
#     sys.stdin = open('simulation/230609_bj_s4_개미/%d.out' % i, 'r')
#     input = sys.stdin.readline
#     print(i, '정답:', input())