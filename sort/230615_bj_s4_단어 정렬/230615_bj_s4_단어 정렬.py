import sys
sys.stdin = open('sort/230615_bj_s4_단어 정렬/1.in', 'r')
input = sys.stdin.readline

def solution():
    N = int(input())

    words = list(set([input() for _ in range(N)]))
    

    def sort_helper(x):
        return len(x), x
    
    words.sort(key=sort_helper)
    print(*words, sep='', end='')

solution()
