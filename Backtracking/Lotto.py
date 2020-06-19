"""
Input:
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0

Output:
1 2 3 4 5 6
1 2 3 4 5 7
1 2 3 4 6 7
1 2 3 5 6 7
1 2 4 5 6 7
1 3 4 5 6 7
2 3 4 5 6 7

1 2 3 5 8 13
1 2 3 5 8 21
1 2 3 5 8 34
1 2 3 5 13 21
1 2 3 5 13 34
1 2 3 5 21 34
1 2 3 8 13 21
1 2 3 8 13 34
1 2 3 8 21 34
1 2 3 13 21 34
1 2 5 8 13 21
1 2 5 8 13 34
1 2 5 8 21 34
1 2 5 13 21 34
1 2 8 13 21 34
1 3 5 8 13 21
1 3 5 8 13 34
1 3 5 8 21 34
1 3 5 13 21 34
1 3 8 13 21 34
1 5 8 13 21 34
2 3 5 8 13 21
2 3 5 8 13 34
2 3 5 8 21 34
2 3 5 13 21 34
2 3 8 13 21 34
2 5 8 13 21 34
3 5 8 13 21 34
"""


# i là vị trí của phần tử thứ i trong mảng res
# p là vị trí của phần tử thứ p trong mảng a
# k là số lượng phần tử trong mảng ban đầu
# lotto_len là độ dài của dãy cần được phát sinh (mặc định bằng 6)
def permutation(i, p, k, lotto_len):
    global a, res
    if i == lotto_len: # Nếu mảng kết quả đã đủ len_lotto = 6 ký tự thì in ra màn hình
        print(*res)
        return

    for j in range(p, k):
        res[i] = a[j] # Lần lượt cố định giá trị res[i] bằng các giá trị từ vị trí p của mảng a trở về sau
        permutation(i + 1, j + 1, k, lotto_len) # Vì vị trí j của mảng a đã được chọn cho res[i], ta xét tiếp từ vị trí (j + 1) trở về sau

res = [None] * 6
blank_line = False

while True:
    k, *a = list(map(int, input().split()))
    if k == 0:
        break
    
    if blank_line:
        print()
    
    permutation(0, 0, k, 6)
    blank_line = True