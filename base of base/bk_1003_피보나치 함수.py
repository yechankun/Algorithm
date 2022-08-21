cnt_zero = [1, 0] + [0] * 39
cnt_one = [0, 1] + [0] * 39

for i in range(2, 41):
    cnt_zero[i] = cnt_zero[i-1] + cnt_zero[i-2]
    cnt_one[i] = cnt_one[i-1] + cnt_one[i-2]

for _ in range(int(input())):
    n = int(input())
    print(cnt_zero[n], cnt_one[n])
