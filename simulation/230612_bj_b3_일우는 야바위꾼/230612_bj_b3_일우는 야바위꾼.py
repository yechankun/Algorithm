import sys
sys.stdin = open('simulation/230608_bj_b3_일우는 야바위꾼/1.in', 'r')
input = sys.stdin.readline

def solution():
    N, X, K = map(int, input().split())

    for _ in range(K):
        a, b = map(int, input().split())
        if a == X:
            X, b = b, X
        elif b == X:
            X, a = a, X
    print(X)
solution()