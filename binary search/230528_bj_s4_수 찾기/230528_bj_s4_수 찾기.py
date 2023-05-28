import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

M =  int(input())
B = list(map(int, input().split()))

A.sort() # 이분 탐색을 위한 정렬
for check in B:
    start, end = 0, N - 1
    while start <= end:
        mid = (start+end) // 2
        if A[mid] == check:
            print(1)
            break
        elif A[mid] < check:
            start = mid + 1
        else:
            end = mid - 1
    else:
        print(0)
