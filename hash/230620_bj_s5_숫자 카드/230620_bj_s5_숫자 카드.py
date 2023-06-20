# 

import sys
sys.stdin = open("./hash/230620_bj_s5_숫자 카드/1.in", "r")
input = sys.stdin.readline

def solution():

    N = int(input())

    numbers = set(map(int, input().rstrip().split()))

    M = int(input())

    checks = list(map(int, input().rstrip().split()))

    answers = [1 if c in numbers else 0 for c in checks]

    print(*answers)

    return

solution()

