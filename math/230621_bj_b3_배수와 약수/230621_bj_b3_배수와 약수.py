# https://www.acmicpc.net/problem/5086

import sys
sys.stdin = open("./math/230621_bj_b3_배수와 약수/1.in", "r")
input = sys.stdin.readline

def solution():
    while True:
        inp = tuple(map(int, input().split()))
        if inp == (0,0):
            break
        N, M = inp
        if M % N == 0:
            print("factor")
        elif N % M == 0:
            print("multiple")
        else:
            print("neither")
    return

solution()
    